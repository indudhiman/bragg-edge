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

import numpy as np

from ibeatles.interfaces.ui_fittingStoryTable import Ui_MainWindow as UiMainWindow
from ibeatles.table_dictionary.table_fitting_story_dictionary_handler import TableFittingStoryDictionaryHandler
from ibeatles.utilities.status import Status


class CreateFittingStoryLauncher(object):
    
    def __init__(self, parent=None):
        self.parent = parent
        
        if self.parent.fitting_story_ui == None:
            fitting_story_window = FittingStoryWindow(parent=parent)
            fitting_story_window.show()
            self.parent.fitting_story_ui = fitting_story_window
        
        else:
            self.parent.fitting_story_ui.setFocus()
            self.parent.fitting_story_ui.activateWindow()
            
            
class FittingStoryWindow(QMainWindow):
    
    list_column_tag = ['d_spacing',
                       'sigma',
                       'alpha',
                       'a1',
                       'a2',
                       'a5',
                       'a6',
                       ]
    
    def __init__(self, parent=None):
        self.parent = parent
        QMainWindow.__init__(self, parent=parent)
        self.ui= UiMainWindow()
        self.ui.setupUi(self)
        
        self.init_widgets()
        self.initialize_table()
        self.fill_table()
        self.select_row(row=0)
        self.check_status_buttons(row=0)
        
    def init_widgets(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MPL Toolbar/up_arrow.png/"))
        self.ui.up_button.setIcon(QtGui.QIcon(icon))
        self.ui.up_button.setEnabled(False)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MPL Toolbar/down_arrow.png/"))
        self.ui.down_button.setIcon(QtGui.QIcon(icon))
        self.ui.down_button.setEnabled(False)
        
    def clear_table(self):
        nbr_row = self.ui.story_table.rowCount()
        for _row in np.arange(nbr_row):
            self.ui.story_table.removeRow(0)
        
    def initialize_table(self):
        if self.parent.table_fitting_story_dictionary == {}:
            o_table = TableFittingStoryDictionaryHandler(parent=self.parent)
            o_table.initialize_table()
        
    def reset_table(self):
        o_table = TableFittingStoryDictionaryHandler(parent=self.parent)
        o_table.initialize_table()
        self.fill_table()
        self.select_row(row=0)
        self.check_status_buttons(row=0)
        
    def fill_table(self):
        table_fitting_story_dictionary = self.parent.table_fitting_story_dictionary
        
        story_table = self.ui.story_table
        
        self.clear_table()
        for _index in table_fitting_story_dictionary.keys():
            story_table.insertRow(_index)
                        
            _entry = table_fitting_story_dictionary[_index]
            
            _status_of_row = _entry['progress']
            if _status_of_row == Status.in_progress:
                _color = QtGui.QColor(0,255,0, alpha=255)
            elif _status_of_row == Status.completed:
                _color = QtGui.QColor(0, 0, 255, alpha=255)
            else:
                _color = QtGui.QColor(0, 0, 0)
            
            #_item = self.set_item(text=str(_index+1))
            #_item.setTextColor(_color)
            #story_table.setItem(_index, 0, _item)
                        
            for _index_tag, _tag in enumerate(self.list_column_tag):
                _widget = self.set_widget(status=_entry[_tag])
                story_table.setCellWidget(_index, _index_tag, _widget)

    def set_item(self, text=''):
        _item = QtGui.QTableWidgetItem(text)
        return _item

    def set_widget(self, status=False):
        _layout = QtGui.QHBoxLayout()
        _widget = QtGui.QCheckBox()
        _widget.setChecked(status)
        _layout.addStretch()
        _layout.addWidget(_widget)
        _layout.addStretch()
        _new_widget = QtGui.QWidget()
        _new_widget.setLayout(_layout)
        return _new_widget
        
    def add_row_button_clicked(self):
        pass
    
    def remove_row_button_clicked(self):
        selection = self.ui.story_table.selectedRanges()[0]
        row = selection.topRow()
    
        o_table_handler = TableFittingStoryDictionaryHandler(parent=self.parent)
        o_table_handler.remove_entry(index_to_remove=row)

        self.fill_table()
        
        #select new row
        nbr_row = self.ui.story_table.rowCount()
        if nbr_row == 0:
            self.check_status_buttons()
            return
            
        elif row == nbr_row:
            new_row_selected = row - 1
        else:
            new_row_selected = row
            
        self.select_row(row = new_row_selected)
        self.check_status_add_remove_buttons()
    
    def start_fitting_button_clicked(self):
        pass

    def _move_row_clicked(self, direction='up'):
        selection = self.ui.story_table.selectedRanges()[0]
        row = selection.topRow()
    
        o_table_handler = TableFittingStoryDictionaryHandler(parent=self.parent)
        o_table_handler.move_entry(current_index_row=row, direction=direction)

        self.fill_table()

        # make selection follows new position of row
        if direction == 'up':
            new_row = row - 1
        else:
            new_row = row + 1
        self.select_row(row=new_row)
        
        self.check_status_buttons(row=new_row)

    def deselect_row(self, row=0):
        self.select_row_status(row=row, status=False)

    def select_row(self, row=0):
        self.select_row_status(row=row, status=True)

    def select_row_status(self, row=0, status=False):
        nbr_column=self.ui.story_table.columnCount()
        _selection = QtGui.QTableWidgetSelectionRange(row, 0, row, nbr_column-1)
        self.ui.story_table.setRangeSelected(_selection, status)

    def move_row_up_clicked(self):
        self._move_row_clicked(direction='up')
    
    def move_row_down_clicked(self):
        self._move_row_clicked(direction='down')

    def cell_clicked(self, row, column):
        self.check_status_buttons(row=row)
        
    def check_status_buttons(self, row=np.NaN):
        '''
        check the enabled status of the arrow buttons according to row clicked
        '''
        nbr_row = self.ui.story_table.rowCount()

        up_status = True
        down_status = True

        print(row)

        if nbr_row == 0:
            down_status = False
            up_status = False
        
        elif row == (nbr_row-1): # we clicked the last row, disable move down
            down_status = False
            
        elif row == 0 : # we can't move up this row
            up_status = False

        elif np.isnan(row):
            up_status = False
            down_status = False
            
        if self.parent.table_fitting_story_dictionary == {}:
            up_status= False
            down_status = False
            
        self.ui.down_button.setEnabled(down_status)
        self.ui.up_button.setEnabled(up_status)
        
        self.check_status_add_remove_buttons()
        
    def check_status_add_remove_buttons(self):
        nbr_row = self.ui.story_table.rowCount()

        add_status = True
        remove_status = True

        if nbr_row == 0:
            remove_status = False
            
        self.ui.add_row_button.setEnabled(add_status)
        self.ui.remove_row_button.setEnabled(remove_status)
        
    def closeEvent(self, event=None):
        self.parent.fitting_story_ui = None