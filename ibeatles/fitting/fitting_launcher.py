try:
    import PyQt4
    import PyQt4.QtGui as QtGui
    import PyQt4.QtCore as QtCore
    from PyQt4.QtGui import QMainWindow
    from PyQt4.QtGui import QApplication         
except:
    import PyQt5
    import PyQt5.QtGui as QtGui
    import PyQt5.QtCore as QtCore
    from PyQt5.QtWidgets import QMainWindow
    from PyQt5.QtWidgets import QApplication

from pyqtgraph.dockarea import *
import pyqtgraph as pg
import numpy as np
    
from ibeatles.interfaces.ui_fittingWindow import Ui_MainWindow as UiMainWindow
from ibeatles.utilities.colors import pen_color
from ibeatles.utilities.array_utilities import find_nearest_index

from ibeatles.fitting.fitting_handler import FittingHandler
from ibeatles.fitting.value_table_handler import ValueTableHandler
from ibeatles.fitting.selected_bin_handler import SelectedBinsHandler
from ibeatles.table_dictionary.table_dictionary_handler import TableDictionaryHandler
from ibeatles.fitting.filling_table_handler import FillingTableHandler


class FittingLauncher(object):
    
    def __init__(self, parent=None):
        self.parent = parent

        if self.parent.fitting_ui == None:
            fitting_window = FittingWindow(parent=parent)
            fitting_window.show()
            self.parent.fitting_ui = fitting_window
            o_fitting = FittingHandler(parent=self.parent)
            o_fitting.display_image()
            o_fitting.display_roi()
            o_fitting.fill_table()
        else:
            self.parent.fitting_ui.setFocus()
            self.parent.fitting_ui.activateWindow()
            
class FittingWindow(QMainWindow):        
    
    data = []
    there_is_a_roi = False
    
    list_bins_selected_item = []
    list_bins_locked_item = []
    
    image_view = None
    bragg_edge_plot = None
    line_view = None
    
    line_view_fitting = None #roi selected in binning window
    all_bins_button = None
    indi_bins_button = None
    
    para_cell_width = 110
    header_table_columns_width = [50,50,100,
                                  para_cell_width, 
                                  para_cell_width,
                                  para_cell_width,
                                  para_cell_width,
                                  para_cell_width,
                                  para_cell_width,
                                  para_cell_width,
                                  para_cell_width,
                                  para_cell_width]
    fitting_table_columns_width = [header_table_columns_width[0],
                                   header_table_columns_width[1],
                                   header_table_columns_width[2],
                                   np.int(header_table_columns_width[3]/2),
                                   np.int(header_table_columns_width[3]/2),
                                   np.int(header_table_columns_width[4]/2),
                                   np.int(header_table_columns_width[4]/2),
                                   np.int(header_table_columns_width[5]/2),
                                   np.int(header_table_columns_width[5]/2),
                                   np.int(header_table_columns_width[6]/2),
                                   np.int(header_table_columns_width[6]/2),
                                   np.int(header_table_columns_width[7]/2),
                                   np.int(header_table_columns_width[7]/2),
                                   np.int(header_table_columns_width[8]/2),
                                   np.int(header_table_columns_width[8]/2),
                                   np.int(header_table_columns_width[9]/2),
                                   np.int(header_table_columns_width[9]/2),
                                   np.int(header_table_columns_width[10]/2),
                                   np.int(header_table_columns_width[10]/2)]

    def __init__(self, parent=None):
        
        self.parent = parent
        QMainWindow.__init__(self, parent=parent)
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("5. Fitting")

        self.init_pyqtgraph()
        self.init_labels()
        self.init_widgets()
        self.init_table_behavior()

    def re_fill_table(self):
        o_fitting = FittingHandler(parent=self.parent)
        o_fitting.fill_table()
        
    def init_table_behavior(self):
        for _column, _width in enumerate(self.header_table_columns_width):
            self.ui.header_table.setColumnWidth(_column, _width)
            
        for _column, _width in enumerate(self.fitting_table_columns_width):
            self.ui.value_table.setColumnWidth(_column, _width)
            
        self.hori_header_table = self.ui.header_table.horizontalHeader()
        self.hori_value_table = self.ui.value_table.horizontalHeader()
        
        self.hori_header_table.sectionResized.connect(self.resizing_header_table)
        self.hori_value_table.sectionResized.connect(self.resizing_value_table)

    def resizing_header_table(self, index_column, old_size, new_size):
        if index_column < 3:
            self.ui.value_table.setColumnWidth(index_column, new_size)
        else:
            new_half_size = np.int(new_size/2)
            index1 = (index_column - 3) * 2 + 3
            index2 = index1+1
            self.ui.value_table.setColumnWidth(index1, new_half_size)
            self.ui.value_table.setColumnWidth(index2, new_half_size)
    
    def resizing_value_table(self, index_column, old_size, new_size):
        if index_column < 3:
            self.ui.header_table.setColumnWidth(index_column, new_size)
        else:
            if (index_column % 2) == 1:
                right_new_size = self.ui.value_table.columnWidth(index_column + 1)
                index_header = np.int(index_column - 3) / 2 + 3
                self.ui.header_table.setColumnWidth(index_header, new_size + right_new_size)
                
            else:
                left_new_size = self.ui.value_table.columnWidth(index_column - 1)
                index_header = np.int(index_column - 4) / 2 + 3
                self.ui.header_table.setColumnWidth(index_header, new_size + left_new_size)
        
    def init_widgets(self):
        '''
        such as material h,k,l list according to material selected in normalized tab
        '''
        hkl_list = self.parent.selected_element_hkl_array
        str_hkl_list = ["{},{},{}".format(_hkl[0], _hkl[1], _hkl[2]) for _hkl in hkl_list]
        self.ui.hkl_list_ui.addItems(str_hkl_list)
        
#        self.installEventFilter(self)
        
    #def eventFilter(self, obj, event):
        #if event.type() == QtCore.QEvent.WindowActivate:
            #self.update_ui()
            #return True
        #return False

    #def update_ui(self):
        
        #if self.parent.binning_line_view['pos'] is None:
            #return
        
        #o_table = TableDictionaryHandler(parent=self.parent)
        #o_table.create_table_dictionary()
        
        #o_fitting = FillingTableHandler(parent=self.parent)
        #o_fitting.fill_table()
        
        #self.parent.fitting_ui.selection_in_value_table_of_rows_cell_clicked(-1, -1)       
        #o_hanlder = FittingHandler(parent=self.parent)
        #o_hanlder.display_roi()

        #self.show_all_widgets()
        
    #def show_all_widgets(self):
        #self.ui.area.setVisible(True)
        
    def init_labels(self):
        self.ui.lambda_min_label.setText(u"\u03BB<sub>min</sub>")
        self.ui.lambda_max_label.setText(u"\u03BB<sub>max</sub>")
        self.ui.lambda_min_units.setText(u"\u212B")
        self.ui.lambda_max_units.setText(u"\u212B")
        self.ui.bragg_edge_units.setText(u"\u212B")
        self.ui.material_groupBox.setTitle(self.parent.selected_element_name)
                
    def init_pyqtgraph(self):

        if (len(self.parent.data_metadata['normalized']['data_live_selection']) > 0) and \
           not (self.parent.binning_line_view['pos'] is None):
            status = True
        else:
            status = False

        area = DockArea()
        self.ui.area = area
        area.setVisible(status)
        d1 = Dock("Image Preview", size=(200, 300))
        d2 = Dock("Bragg Edge", size=(200, 100))
    
        area.addDock(d1, 'top')
        area.addDock(d2, 'bottom')
    
        preview_widget = pg.GraphicsLayoutWidget()
        pg.setConfigOptions(antialias=True) # this improve display
    
        vertical_layout = QtGui.QVBoxLayout()
        preview_widget.setLayout(vertical_layout)
    
        # image view (top plot)
        image_view = pg.ImageView()
        image_view.ui.roiBtn.hide()
        image_view.ui.menuBtn.hide()
        self.image_view = image_view
        image_view.scene.sigMouseMoved.connect(self.mouse_moved_in_image_view)
       
        top_widget = QtGui.QWidget()
        vertical = QtGui.QVBoxLayout()
        vertical.addWidget(image_view)

        # bin transparency
        transparency_layout = QtGui.QHBoxLayout()
        spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        transparency_layout.addItem(spacer)        
        label = QtGui.QLabel("Bin Transparency")
        transparency_layout.addWidget(label)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        slider.setMaximum(100)
        slider.setMinimum(0)
        slider.setValue(50)
        slider.valueChanged.connect(self.slider_changed)
        self.slider = slider
        transparency_layout.addWidget(slider)
        bottom_widget = QtGui.QWidget()
        bottom_widget.setLayout(transparency_layout)

        top_widget.setLayout(vertical)
        d1.addWidget(top_widget)
        d1.addWidget(bottom_widget)
    
        # bragg edge plot (bottom plot)
        bragg_edge_plot = pg.PlotWidget(title='')
        bragg_edge_plot.plot()
        self.bragg_edge_plot = bragg_edge_plot
    
        # plot all or individual bins
        buttons_layout = QtGui.QHBoxLayout()
        spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        buttons_layout.addItem(spacer)
        label = QtGui.QLabel("Plots Bins")
        label.setEnabled(False)
        buttons_layout.addWidget(label)
        
        # all bins button
        all_button = QtGui.QRadioButton()
        all_button.setText("All")
        all_button.setChecked(True)
        all_button.setEnabled(False)
        all_button.pressed.connect(self.plots_bins_all_pressed)
        self.all_bins_button = all_button
        
        # indi bin button
        buttons_layout.addWidget(all_button)
        indi_button = QtGui.QRadioButton()
        indi_button.setText("Individual")
        indi_button.setChecked(False)
        indi_button.setEnabled(False)
        indi_button.pressed.connect(self.plots_bins_individual_pressed)
        self.indi_bins_button = indi_button

        buttons_layout.addWidget(indi_button)
        bottom_widget = QtGui.QWidget()
        bottom_widget.setLayout(buttons_layout)
    
        d2.addWidget(bragg_edge_plot)
        d2.addWidget(bottom_widget)
    
        vertical_layout.addWidget(area)
        self.ui.widget.setLayout(vertical_layout)        
        
    def mouse_moved_in_image_view(self):
        self.image_view.setFocus(True)        
        
    def plots_bins_all_pressed(self):
        print("all pressed")
        
    def plots_bins_individual_pressed(self):
        print("indi pressed")
        
    def hkl_list_changed(self, hkl):
        bragg_edges_array = self.parent.selected_element_bragg_edges_array
        if bragg_edges_array:
            if str(hkl) == '':
                value = "N/A"
            else:
                hkl_array = self.parent.selected_element_hkl_array
                str_hkl_list = ["{},{},{}".format(_hkl[0], _hkl[1], _hkl[2]) for _hkl in hkl_array]
                hkl_bragg_edges = dict(zip(str_hkl_list, bragg_edges_array))
                value = "{:04.3f}".format(hkl_bragg_edges[str(hkl)])
        else:
            value = "N/A"
        self.ui.bragg_edge_calculated.setText(value)
        
    def slider_changed(self):
        o_fitting_handler = FittingHandler(parent=self.parent)
        o_fitting_handler.display_roi()

    def lock_button_state_changed(self, status, row_clicked):
        '''
        status: 0: off
                2: on
        '''
        if self.parent.advanced_selection_ui:
            self.parent.advanced_selection_ui.ui.lock_table.blockSignals(True)

        # retrieve selection
        selection = self.ui.value_table.selectedRanges()
        nbr_selection = len(selection)

        # make sure the row is inside the selection
        click_inside_selection = False
        for _select in selection:
            top_row = _select.topRow()
            bottom_row = _select.bottomRow()
            if (row_clicked <= bottom_row) and (row_clicked >= top_row):
                click_inside_selection = True
                break

        if click_inside_selection:
            for _select in selection:
                top_row = _select.topRow()
                bottom_row = _select.bottomRow()
                
                for _row in np.arange(top_row, bottom_row+1):
                    _widget = self.ui.value_table.cellWidget(_row, 0)
                    _widget.blockSignals(True)
                    if status == 0:
                        _widget.setChecked(False)
                    else:
                        _widget.setChecked(True)
                    _widget.blockSignals(False)
                        
        o_bin_handler = SelectedBinsHandler(parent = self.parent)
        o_bin_handler.update_bins_selected()
        o_bin_handler.update_bins_locked()
        
        if self.parent.advanced_selection_ui:
            self.parent.advanced_selection_ui.update_selection_table()
            self.parent.advanced_selection_ui.update_lock_table()
            self.parent.advanced_selection_ui.ui.lock_table.blockSignals(False)
        
    def value_table_right_click(self, position):
        o_table_handler = ValueTableHandler(parent=self.parent)
        o_table_handler.right_click(position=position)
    
    def update_image_view_selection(self):
        o_bin_handler = SelectedBinsHandler(parent = self.parent)
        o_bin_handler.update_bins_selected()
        
    def update_image_view_lock(self):
        o_bin_handler = SelectedBinsHandler(parent = self.parent)
        o_bin_handler.update_bins_locked()
        
    def update_bragg_edge_plot(self):
        o_bin_handler = SelectedBinsHandler(parent = self.parent)
        o_bin_handler.update_bragg_edge_plot()

    def selection_in_value_table_of_rows_cell_clicked(self, row, column):
        pass            
        #self.update_image_view_selection()
        #self.update_image_view_lock()
        #if self.parent.advanced_selection_ui:
            #self.parent.advanced_selection_ui.update_selection_table()
            #self.parent.advanced_selection_ui.update_lock_table()
        #self.update_bragg_edge_plot()
        
    def selection_in_value_table_changed(self):
        try:
            self.selection_in_value_table_of_rows_cell_clicked(-1, -1)
        except:
            pass
        
    def bragg_edge_linear_region_changed(self):

        #current xaxis is
        x_axis = self.parent.fitting_bragg_edge_x_axis
        _lr = self.parent.fitting_lr
        selection = list(_lr.getRegion())
    
        left_index = find_nearest_index(array = x_axis, value=selection[0])
        right_index = find_nearest_index(array = x_axis, value=selection[1])
    
        list_selected = [left_index, right_index]
        self.parent.fitting_bragg_edge_linear_selection = list_selected
        
    def advanced_table_clicked(self, status):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        o_table_handler = FillingTableHandler(parent=self.parent)
        o_table_handler.set_mode(advanced_mode = status)
        QApplication.restoreOverrideCursor()
        
    def closeEvent(self, event=None):
        self.parent.fitting_ui = None
    