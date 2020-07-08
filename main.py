import sys
from PyQt5 import QtWidgets,QtGui,QtCore
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor as QVTKWidget

__version__='0.1.0'
__author__ ='wbl'
__appname__='PyPost'


class PyPostMainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(PyPostMainWindow,self).__init__()

        self.create_widgets()
        self.create_menu()
        self.load_settings()
        self.init_vtk_view()
        self.deformation_actor=None
        self.outline_actor=None

        self.setWindowTitle("{} -v{}".format(__appname__,__version__))

    # 重写关闭事件
    def closeEvent(self,event):
        settings=QtCore.QSettings()
        settings.setValue('MainWindow/Geometry',QtCore.QVariant(self.saveGeometry()))
        settings.setValue('MainWindow/State',QtCore.QVariant(self.saveState()))

    def create_widgets(self):
        # 实例化一个QWidget，用作中心部件
        self.central_widget=QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        # 
        self.tab_widget=QtWidgets.QTabWidget(self.central_widget)
        self.tab_widget.setObjectName("tab_widget")
        size_policy=QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(size_policy)
        #
        self.set_result_tab()
        #
        self.main_widget=QtWidgets.QWidget(self.central_widget)
        self.main_widget.setObjectName("main_widget")
        #
        self.vertical_layout=QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName("vertical_layout")
        self.vertical_layout.addWidget(self.tab_widget)
        self.vertical_layout.addWidget(self.main_widget)
        self.setCentralWidget(self.central_widget)

    def create_menu(self):
        self.setup_file_menu()
        self.setup_view_menu()
        self.setup_help_menu()
        status=self.statusBar()
        status.setSizeGripEnabled(True)

    # 加载配置
    def load_settings(self):
        settings=QtCore.QSettings()
        self.restoreGeometry(settings.value('MainWindow/Geometry',type=QtCore.QByteArray))
        self.restoreState(settings.value('MainWindow/State',type=QtCore.QByteArray))

    def init_vtk_view(self):
        self.vtk_vertical_layout=QtWidgets.QVBoxLayout(self.main_widget)
        self.vtk_widget=QVTKWidget(self.main_widget)
        self.vertical_layout.addWidget(self.vtk_widget)

        self.renderer_window=self.vtk_widget.GetRenderWindow()
        self.renderer=vtk.vtkRenderer()
        self.renderer.SetBackground(1.0,1.0,1.0)
        self.renderer_window.AddRenderer(self.renderer)
        self.renderer_window.Render()
        self.iren=self.renderer_window.GetInteractor()
        self.style=vtk.vtkInteractorStyleTrackballCamera()
        self.iren.SetInteractorStyle(self.style)
        
    def set_result_tab(self):
        # tab widget
        self.result_tab=QtWidgets.QWidget()
        self.result_tab.setObjectName("result_tab")
        # 
        self.result_grid_layout=QtWidgets.QGridLayout(self.result_tab)
        self.result_grid_layout.setObjectName("result_grid_layout")
        # 
        self.deformation_horizontal_layout=QtWidgets.QHBoxLayout()
        self.deformation_horizontal_layout.setObjectName("deformation_horizontal_layout")
        #
        self.deformation_check_box=QtWidgets.QCheckBox(self.result_tab)
        self.deformation_check_box.setObjectName("deformation_check_box")
        self.deformation_check_box.setText("变形")
        self.deformation_check_box.stateChanged.connect(self.draw_displacement)
        #
        self.deformation_combo_box=QtWidgets.QComboBox(self.result_tab)
        self.deformation_combo_box.setObjectName("deformation_combo_box")
        self.deformation_combo_box.addItem("仅显示变形")
        self.deformation_combo_box.addItem("初始轮廓+变形")
        self.deformation_combo_box.currentTextChanged.connect(self.draw_displacement)
        # 
        self.deformation_scale_spinbox=QtWidgets.QDoubleSpinBox(self.result_tab)
        self.deformation_scale_spinbox.setObjectName("deformation_scale_spinbox")
        self.deformation_scale_spinbox.setPrefix("缩放")
        self.deformation_scale_spinbox.setSuffix("倍")
        self.deformation_scale_spinbox.setDecimals(4)
        self.deformation_scale_spinbox.setValue(1)
        self.deformation_scale_spinbox.valueChanged.connect(self.draw_displacement)
        #
        deformation_spacer_item=QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,
        QtWidgets.QSizePolicy.Minimum)

        self.deformation_horizontal_layout.addWidget(self.deformation_check_box)
        self.deformation_horizontal_layout.addWidget(self.deformation_combo_box)
        self.deformation_horizontal_layout.addWidget(self.deformation_scale_spinbox)
        self.deformation_horizontal_layout.addItem(deformation_spacer_item)
        # 
        self.contour_horizontal_layout=QtWidgets.QHBoxLayout()
        self.contour_horizontal_layout.setObjectName("contour_horizontal_layout")
        #
        self.contour_check_box=QtWidgets.QCheckBox(self.result_tab)
        self.contour_check_box.setObjectName("contour_check_box")
        self.contour_check_box.setText("云图")
        self.contour_check_box.stateChanged.connect(self.draw_contour)
        #
        self.contour_combo_box=QtWidgets.QComboBox(self.result_tab)
        self.contour_combo_box.setObjectName("contour_combo_box")
        self.contour_combo_box.addItem("总变形")
        self.contour_combo_box.addItem("x方向变形")
        self.contour_combo_box.addItem("y方向变形")
        self.contour_combo_box.addItem("z方向变形")
        self.contour_combo_box.addItem("Mises应力")
        self.contour_combo_box.currentTextChanged.connect(self.draw_contour)
        #
        contour_spacer_item=QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.contour_horizontal_layout.addWidget(self.contour_check_box)
        self.contour_horizontal_layout.addWidget(self.contour_combo_box)
        self.contour_horizontal_layout.addItem(contour_spacer_item)
        #
        self.result_grid_layout.addLayout(self.deformation_horizontal_layout,0,1,1,1)
        self.result_grid_layout.addLayout(self.contour_horizontal_layout,1,1,1,1)
        self.tab_widget.addTab(self.result_tab,"结果")

    def create_action(self,text,slot=None,shotcut=None,icon=None,tip=None,checkable=False,signal='triggered'):
        
        action=QtWidgets.QAction(text,self)
        if icon is not None:
            action.setIcon(QtGui.QIcon(icon))
        if shotcut is not None:
            action.setShortcut(shotcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            getattr(action,signal).connect(slot)
        if checkable:
            action.setCheckable(True)
        return action

    def setup_file_menu(self):

        file_menu=self.menuBar().addMenu("文件")
        file_toolbar=self.addToolBar("文件")
        file_toolbar.setObjectName("file_toolbar")
        file_open_action=self.create_action("打开",self.file_open,QtGui.QKeySequence.Open,'images/open','打开文件')
        file_quit_action=self.create_action("退出",self.close,'CTRL+Q','images/exit',"退出")
        self.add_actions(file_menu,(file_open_action,None,file_quit_action))
        self.add_actions(file_toolbar,(file_open_action,file_quit_action))

    def setup_view_menu(self):
        view_menu=self.menuBar().addMenu("视图")
        view_toolbar=self.addToolBar("视图")
        view_toolbar.setObjectName("view_toolbar")
        view_fit_action=self.create_action('适合窗口',self.fit_all,'CTRL+F','images/fit','适合窗口')
        self.add_actions(view_menu,(view_fit_action,))
        self.add_actions(view_toolbar,(view_fit_action,))

    def setup_help_menu(self):
        help_menu=self.menuBar().addMenu("帮助")
        help_action=self.create_action("帮助",self.help,icon='images/help',tip='帮助')
        about_action=self.create_action('关于',self.about,tip="关于")
        self.add_actions(help_menu,(help_action,about_action))


    def add_actions(self,target,actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def file_open(self):
        self.filename,_=QtWidgets.QFileDialog.getOpenFileName(self,'打开文件 - vtk文件','.','(*.vtk)')
        if self.filename:
            self.original_model=vtk.vtkPolyDataReader()
            self.original_model.SetFileName(self.filename)
            self.original_model.Update()

            self.original_mapper=vtk.vtkPolyDataMapper()
            self.original_mapper.SetInputConnection(self.original_model.GetOutputPort())

            self.original_actor=vtk.vtkActor()
            self.original_actor.SetMapper(self.original_mapper)
            self.original_actor.GetProperty().SetColor(0.5,0.5,0.0)

            self.renderer.AddActor(self.original_actor)
            self.renderer.ResetCamera()

    def fit_all(self):
        self.renderer.ResetCamera()
        self.renderer_window.Render()

    def help(self):
        QtWidgets.QMessageBox.information(self,"Help","please open <a>https://github.com/wblong</a>",QtWidgets.QMessageBox.Yes)

    def about(self):
        QtWidgets.QMessageBox.about(self,self.tr("关于PyPost"),""" <b>PyPost</b> v{} by {}""".format(__version__,__author__))

    def draw_displacement(self):
        if self.filename:
            show_displacement=self.deformation_check_box.isChecked()
            if show_displacement:
                self.original_actor.VisibilityOff()
                if not self.deformation_actor:
                    self.original_model.SetVectorsName("mode1")
                    self.normals=vtk.vtkPolyDataNormals()
                    self.normals.SetInputConnection(self.original_model.GetOutputPort())
                    self.warp=vtk.vtkWarpVector()
                    self.warp.SetInputConnection(self.normals.GetOutputPort())

                    deformation_mapper=vtk.vtkDataSetMapper()
                    deformation_mapper.SetInputConnection(self.warp.GetOutputPort())
                    self.deformation_actor=vtk.vtkActor()
                    self.deformation_actor.SetMapper(deformation_mapper)
                    self.deformation_actor.GetProperty().SetColor(0.5,0.5,0.5)
                    self.renderer.AddActor(self.deformation_actor)

                factor=self.deformation_scale_spinbox.value()
                self.warp.SetScaleFactor(factor)

                if self.deformation_combo_box.currentText()== "仅显示变形":
                    if self.outline_actor:
                        self.outline_actor.VisibilityOff()
                    self.deformation_actor.VisibilityOn()
                elif self.deformation_combo_box.currentText()=="初始轮廓+变形":
                    if self.outline_actor:
                        self.outline_actor.VisibilityOn()
                    else:
                        outline=vtk.vtkOutlineFilter()
                        outline.SetInputConnection(self.original_model.GetOutputPort())
                        outline_mapper=vtk.vtkPolyDataMapper()
                        outline_mapper.SetInputConnection(outline.GetOutputPort())
                        self.outline_actor=vtk.vtkActor()
                        self.outline_actor.SetMapper(outline_mapper)
                        self.outline_actor.GetProperty().SetColor(1.0,0.5,0.5)
                        self.renderer.AddActor(self.outline_actor)
            else:
                if self.deformation_actor:
                    self.deformation_actor.VisibilityOff()
                if self.outline_actor:
                    self.outline_actor.VisibilityOff()
                self.original_actor.VisibilityOn()
            self.renderer_window.Render()  

    def draw_contour(self):
        pass
if __name__ == '__main__':

    app=QtWidgets.QApplication(sys.argv)
    app.setApplicationName('{}'.format(__appname__))
    app.setOrganizationName('ctkj')
    win=PyPostMainWindow()
    win.show()
    app.exec()