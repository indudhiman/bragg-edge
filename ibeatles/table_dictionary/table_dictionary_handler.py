import numpy as np
try:
    import PyQt4.QtGui as QtGui
    import PyQt4.QtCore as QtCore
    from PyQt4.QtGui import QApplication 
except:
    import PyQt5.QtGui as QtGui
    import PyQt5.QtCore as QtCore
    from PyQt5.QtWidgets import QApplication

import os
import pyqtgraph as pg
import pandas as pd

import ibeatles.fitting.fitting_handler
from ibeatles.utilities.array_utilities import get_min_max_xy
from ibeatles.utilities.math_tools import get_random_value


class TableDictionaryHandler(object):
        
    selected_color = {'pen': (0,0,0,30),
                      'brush': (0,255,0,150)}

    lock_color = {'pen': (0,0,0,30),
                  'brush': (255,0,0,240)}

    header = ['x0','y0','x1','y1','row_index','column_index','lock','active',
                      'fitting_confidence','d_spacing_value','d_spacing_err','d_spacing_fixed',
                      'sigma_value','sigma_err','sigma_fixed',
                      'intensity_value','intensity_err','intensity_fixed',
                      'alpha_value','alpha_err','alpha_fixed',
                      'a1_value','a1_err','a1_fixed',
                      'a2_value','a2_err','a2_fixed',
                      'a5_value','a5_err','a5_fixed',
                      'a6_value','a6_err','a6_fixed']    
    
    def __init__(self, parent=None):
        self.parent = parent
        
    def fill_table_with_variable(self, variable_name='d_spacing', value=np.NaN, list_keys=[], all_keys=False):
        table_dictionary = self.parent.table_dictionary
        if all_keys:
            list_keys = table_dictionary.keys()
            
        for _key in list_keys:
            table_dictionary[_key][variable_name]['val'] = value
            
        self.parent.table_dictionary = table_dictionary
        
    def populate_table_dictionary_entry(self, index=0, array=[]):
        table_dictionary = self.parent.table_dictionary
        
        table_dictionary[str(index)] = {'bin_coordinates': {'x0': array[0],
                                                            'x1': array[2],
                                                            'y0': array[1],
                                                            'y1': array[3]},
                                        'selected_item': None,
                                        'locked_item': None,
                                        'row_index': array[4],
                                        'column_index': array[5],
                                        'selected': False,
                                        'lock': array[6],
                                        'active': array[7],
                                        'fitting_confidence': array[8],
                                        'd_spacing': {'val': array[9], 
                                                      'err': array[10],
                                                      'fixed': array[11]},
                                        'sigma': {'val': array[12], 
                                                  'err': array[13],
                                                  'fixed': array[14]},
                                        'intensity': {'val': array[15], 
                                                      'err': array[16],
                                                      'fixed': array[17]},
                                        'alpha': {'val': array[18], 
                                                  'err': array[19],
                                                  'fixed': array[20]},
                                        'a1': {'val': array[21], 
                                               'err': array[22],
                                               'fixed': array[23]},
                                        'a2': {'val': array[24], 
                                               'err': array[25],
                                               'fixed': array[26]},
                                        'a5': {'val': array[27], 
                                               'err': array[28],
                                               'fixed': array[29]},
                                        'a6': {'val': array[30], 
                                               'err': array[31],
                                               'fixed': array[32]},
                                        }   

        self.parent.table_dictionary = table_dictionary
        
    def create_table_dictionary(self):
        '''
        this will define the corner position and index of each cell
        '''
        if len(np.array(self.parent.data_metadata['normalized']['data_live_selection'])) == 0:
            return

        if not self.parent.table_dictionary == {}:
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
                
                table_dictionary[_str_index] = {'bin_coordinates': {'x0': np.NaN,
                                                                    'x1': np.NaN,
                                                                    'y0': np.NaN,
                                                                    'y1': np.NaN},
                                                'selected_item': None,
                                                'locked_item': None,
                                                'row_index': _index_row,
                                                'column_index': _index_col,
                                                'selected': False,
                                                'lock': False,
                                                'active': False,
                                                'fitting_confidence': np.NaN,
                                                'd_spacing': {'val': np.NaN, 
                                                              'err': np.NaN,
                                                              'fixed': False},
                                                'sigma': {'val': np.NaN, 
                                                          'err': np.NaN,
                                                          'fixed': False},
                                                'intensity': {'val': np.NaN, 
                                                              'err': np.NaN,
                                                              'fixed': False},
                                                'alpha': {'val': np.NaN, 
                                                          'err': np.NaN,
                                                          'fixed': False},
                                                'a1': {'val': np.NaN, 
                                                       'err': np.NaN,
                                                       'fixed': False},
                                                'a2': {'val': np.NaN, 
                                                       'err': np.NaN,
                                                       'fixed': False},
                                                'a5': {'val': np.NaN, 
                                                       'err': np.NaN,
                                                       'fixed': False},
                                                'a6': {'val': np.NaN, 
                                                       'err': np.NaN,
                                                       'fixed': False},
                                                }   
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
                
        table_dictionary = self.parent.table_dictionary
        for _index in table_dictionary:
            _item = table_dictionary[_index]
            _item['active'] = status
            table_dictionary[_index] = _item
            
        self.parent.table_dictionary = table_dictionary
                
    def unselect_full_table(self):
        self.full_table_selection_tool(status = False)

    def select_full_table(self):
        self.full_table_selection_tool(status = True)

    def get_average_parameters_activated(self):
        table_dictionary = self.parent.table_dictionary
        
        d_spacing = []
        alpha = []
        sigma = []
        a1 = []
        a2 = []
        a5 = []
        a6 = []
        
        for _index in table_dictionary.keys():
            _entry = table_dictionary[_index]
            
            if _entry['active']:
                _d_spacing = _entry['d_spacing']['val']
                _alpha = _entry['alpha']['val']
                _sigma = _entry['sigma']['val']
                _a1 = _entry['a1']['val']
                _a2 = _entry['a2']['val']
                _a5 = _entry['a5']['val']
                _a6 = _entry['a6']['val']
            
                d_spacing.append(_d_spacing)
                alpha.append(_alpha)
                sigma.append(_sigma)
                a1.append(_a1)
                a2.append(_a2)
                a5.append(_a5)
                a6.append(_a6)

        mean_d_spacing = self.get_mean_value(d_spacing)
        mean_alpha = self.get_mean_value(alpha)
        mean_sigma = self.get_mean_value(sigma)
        mean_a1 = self.get_mean_value(a1)
        mean_a2 = self.get_mean_value(a2)
        mean_a5 = self.get_mean_value(a5)
        mean_a6 = self.get_mean_value(a6)

        return {'d_spacing': mean_d_spacing, 
                'alpha': mean_alpha,
                'sigma': mean_sigma,
                'a1': mean_a1,
                'a2': mean_a2,
                'a5': mean_a5,
                'a6': mean_a6}
            
    def get_mean_value(self, array=[]):
        if array == []:
            return np.NaN
        else:
            return np.nanmean(array)
        
    def import_table(self):
        default_file_name = str(self.parent.ui.normalized_folder.text()) + '_fitting_table.csv'
        table_file = str(QtGui.QFileDialog.getOpenFileName(self.parent, 
                                                              'Define Location and File Name Where to Export the Table!',
                                                              os.path.join(self.parent.normalized_folder, default_file_name)))
    
    
        if table_file:
            pandas_data_frame = pd.read_csv(table_file)
            o_table = TableDictionaryHandler(parent=self.parent)

            numpy_table = pandas_data_frame.values
            # loop over each row in the pandas data frame
            for _index, _row_values in enumerate(numpy_table):
                o_table.populate_table_dictionary_entry(index=_index,
                                                        array=_row_values)
            
            o_fitting = ibeatles.fitting.fitting_handler.FittingHandler(parent=self.parent)
            o_fitting.fill_table()
        
        
        
    def export_table(self):
        default_file_name = str(self.parent.ui.normalized_folder.text()) + '_fitting_table.csv'
        table_file = str(QtGui.QFileDialog.getSaveFileName(self.parent, 
                                                               'Select or Define Name of File!',
                                                               default_file_name,
                                                               "CSV (*.csv)"))
    
        if table_file:  
            table_dictionary = self.parent.table_dictionary
            o_table_formated = FormatTableForExport(table=table_dictionary)
            pandas_data_frame = o_table_formated.pandas_data_frame
            header = self.header
            pandas_data_frame.to_csv(table_file, header=header)
            
class FormatTableForExport(object):
    
    pandas_data_frame = []
    
    def __init__(self, table={}):
        
        pandas_table = []
        
        for _key in table:
            
            _entry = table[_key]
            
            x0 = _entry['bin_coordinates']['x0']
            y0 = _entry['bin_coordinates']['y0']
            x1 = _entry['bin_coordinates']['x1']
            y1 = _entry['bin_coordinates']['y1']
            
            row_index = _entry['row_index']
            column_index = _entry['column_index']
            
            lock = _entry['lock']
            active = _entry['active']
            
            fitting_confidence = _entry['fitting_confidence']
            
            [d_spacing_val,
             d_spacing_err,
             d_spacing_fixed] = self.get_val_err_fixed(_entry['d_spacing'])
        
            [sigma_val,
             sigma_err,
             sigma_fixed] = self.get_val_err_fixed(_entry['sigma'])
            
            [intensity_val,
             intensity_err,
             intensity_fixed] = self.get_val_err_fixed(_entry['intensity'])
            
            [alpha_val,
             alpha_err,
             alpha_fixed] = self.get_val_err_fixed(_entry['alpha'])
            
            [a1_val,
             a1_err,
             a1_fixed] = self.get_val_err_fixed(_entry['a1'])
            
            [a2_val,
             a2_err,
             a2_fixed] = self.get_val_err_fixed(_entry['a2'])
            
            [a5_val,
            a5_err,
            a5_fixed] = self.get_val_err_fixed(_entry['a5'])
        
            [a6_val,
             a6_err,
             a6_fixed] = self.get_val_err_fixed(_entry['a6'])
        
            _row = [x0, x1, y0, y1, 
                    row_index, column_index,
                    lock, active,
                    fitting_confidence,
                    d_spacing_val, d_spacing_err, d_spacing_fixed,
                    sigma_val, sigma_err, sigma_fixed,
                    intensity_val, intensity_err, intensity_fixed,
                    alpha_val, alpha_err, alpha_fixed,
                    a1_val, a1_err, a1_fixed,
                    a2_val, a2_err, a2_fixed,
                    a5_val, a5_err, a5_fixed,
                    a6_val, a6_err, a6_fixed,
                    ]
            
            pandas_table.append(_row)
            
        pandas_data_frame = pd.DataFrame.from_dict(pandas_table)
        self.pandas_data_frame = pandas_data_frame
        
    def get_val_err_fixed(self, item):
        return [item['val'], item['err'], item['fixed']]
