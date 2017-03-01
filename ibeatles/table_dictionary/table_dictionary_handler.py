import numpy as np
from PyQt4 import QtGui
import pyqtgraph as pg

from ibeatles.utilities.array_utilities import get_min_max_xy


class TableDictionaryHandler(object):
        
    selected_color = {'pen': (0,0,0,30),
                      'brush': (0,255,0,150)}

    lock_color = {'pen': (0,0,0,30),
                  'brush': (255,0,0,240)}

    
    def __init__(self, parent=None):
        self.parent = parent
        
    def create_table_dictionary(self):
        '''
        this will define the corner position and index of each cell
        '''
        if len(np.array(self.parent.data_metadata['normalized']['data_live_selection'])) == 0:
            return

        bin_size = self.parent.binning_bin_size
        pos = self.parent.binning_line_view['pos']
        
        # calculate outside real edges of bins
        min_max_xy = get_min_max_xy(pos)
        
        from_x = min_max_xy['x']['min']
        to_x = min_max_xy['x']['max']
        
        from_y = min_max_xy['y']['min']
        to_y = min_max_xy['y']['max']
        
        table_dictionary = {}
        _index = 0
        _index_col = 0
        for _x in np.arange(from_x, to_x, bin_size):
            _index_row = 0
            for _y in np.arange(from_y, to_y, bin_size):
                _str_index = str(_index)
                table_dictionary[_str_index] = {'bin_coordinates': {'x0': -1,
                                                                    'x1': -1,
                                                                    'y0': -1,
                                                                    'y1': -1},
                                                'selected_item': None,
                                                'locked_item': None,
                                                'row_index': _index_row,
                                                'column_index': _index_col,
                                                'selected': False,
                                                'lock': False,
                                                'fitting_confidence': -1,
                                                'd_spacing': {'val': -1, 'err': -1},
                                                'sigma': {'val': -1, 'err': -1},
                                                'intensity': {'val': -1, 'err': -1},
                                                'alpha': {'val': -1, 'err': -1},
                                                'a1': {'val': -1, 'err': -1},
                                                'a2': {'val': -1, 'err': -1},
                                                'a5': {'val': -1, 'err': -1},
                                                'a6': {'val': -1, 'err': -1}}   
                table_dictionary[_str_index]['bin_coordinates']['x0'] = _x
                table_dictionary[_str_index]['bin_coordinates']['x1'] = _x + bin_size
                table_dictionary[_str_index]['bin_coordinates']['y0'] = _y
                table_dictionary[_str_index]['bin_coordinates']['y1'] = _y + bin_size

                # create the box to show when bin is selected
                selection_box = pg.QtGui.QGraphicsRectItem(_x, _y, 
                                                           bin_size,
                                                           bin_size)
                selection_box.setPen(pg.mkPen(self.selected_color['pen']))
                selection_box.setBrush(pg.mkBrush(self.selected_color['brush']))
                table_dictionary[_str_index]['selected_item'] = selection_box

                # create the box to show when bin is locked
                lock_box = pg.QtGui.QGraphicsRectItem(_x, _y, 
                                                           bin_size,
                                                           bin_size)
                lock_box.setPen(pg.mkPen(self.lock_color['pen']))
                lock_box.setBrush(pg.mkBrush(self.lock_color['brush']))
                table_dictionary[_str_index]['locked_item'] = lock_box

                _index += 1
                _index_row += 1

            _index_col += 1
        
        self.parent.table_dictionary = table_dictionary

        #self.parent.fitting_ui.table_dictionary = table_dictionary

        self.parent.fitting_selection['nbr_row'] = _index_row
        self.parent.fitting_selection['nbr_column'] = _index_col    
        
    def full_table_selection_tool(self, status=True):
        
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        
        table_dictionary = self.parent.table_dictionary
        for _index in table_dictionary:
            _item = table_dictionary[_index]
            _item['selected'] = status
            table_dictionary[_index] = _item
            
        self.parent.table_dictionary = table_dictionary
                
        QApplication.restoreOverrideCursor()

    def unselect_full_table(self):
        self.full_table_selection_tool(status = False)

    def select_full_table(self):
        self.full_table_selection_tool(status = True)
