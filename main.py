import kivymd
import kivy
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty
from kivymd.uix.label import MDIcon,MDLabel
from kivymd.uix.button import MDFlatButton, MDTextButton
from kivymd.icon_definitions import md_icons
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.toolbar import MDTopAppBar,MDBottomAppBar,MDActionOverFlowButton
from kivy.properties import ListProperty
from kivy.uix.image import Image
from kivymd.uix.fitimage import FitImage
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.list import MDList, TwoLineAvatarListItem, TwoLineListItem,OneLineListItem,ThreeLineListItem,ThreeLineAvatarListItem,ImageLeftWidget
from kivy.core.window import Window
from kivymd.uix.screenmanager import MDScreenManager, ScreenManager
from kivymd.uix.bottomnavigation import MDBottomNavigation,MDBottomNavigationItem
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel,MDIcon
from kivy.lang.builder import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.widget import MDWidget
from kivy.uix.widget import Widget
from kivy.graphics import RoundedRectangle, Rectangle, Ellipse
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivy.uix.anchorlayout import AnchorLayout


Window.size = (340, 630)
screen_helper = """
MDScreenManager:



    Screen1:
    Screen2:
    Screen3:
    Screen5:
    Screen6:
    Screen7:
    Screen8:
 

            
            
<Screen1>:
    name:"page_1"
    MDFloatLayout:
    
        FitImage:
            source:"s.png"
            allow_stretch:"true"
            keep_ratio:"false"
        MDBoxLayout:
            Image:
                source:
                    "sn.gif"
                pos_hint:{"y":0.2}


<Screen2>:                
    name:"page 2"
    MDBottomNavigation:
        panel_color:(56/255,40/255,81/255,1)
    
       
        MDBottomNavigationItem:
            name:"page 2"
            text:"Home"
            icon:"home"
            
            MDFloatLayout:
                md_bg_color: (56/255,40/255,81/255,1)
                
              
               
               
                   
                  
                MDBoxLayout:
                    orientation:"vertical"
                    md_bg_color: (56/255,40/255,81/255,1)
                    pos_hint: {"top":1}
                    size_hint: 1, 0.1 
                    MDTopAppBar:
                        elevation: 0
                        md_bg_color: (56/255,40/255,81/255,1)
                        pos_hint: {"top":1}
                        title:      "LEVEL ONE COURSES"
                        left_action_items:[["menu", lambda x: nav_drawer.set_state("open")]]
                        right_action_items:[["home"]]
                        
                 
                MDBoxLayout:
                    orientation:"vertical"
                    md_bg_color:(0.6,.8,.6,.3)
                    size_hint: 1,0.9
                    pos_hint: {"top":0.9}
                    radius:30
                    #spacing: "10dp"
                    padding:("10dp","10dp","10dp","10dp")
                    MDScrollView:
                        #md_bg_color: (56/255,40/255,81/255,1)
                        #radius:30
                        do_scroll_y: True
                        do_scroll_x: False
                        radius:30
                        MDFloatLayout:
                            do_scroll_y: True
                            do_scroll_x: False
                            #orientation:"vertical"
                            #md_bg_color: (56/255,40/255,81/255,1)
                            size_hint:1,None
                            height:700
                            radius:30
                            #spacing: "10dp"
                            
                            MDBoxLayout:
                                orientation:
                                    "vertical"
                                md_bg_color: (56/255,40/255,81/255,1)
                                size_hint_y: 0.1
                                size_hint_x: 1
                                pos_hint:{"top":1}
                                radius: 30
                                TwoLineAvatarListItem:
                                    text: "LEVEL 100 1301 V1"
                                    secondary_text:"Questions"
                                    ImageLeftWidget:
                                        source:"icon.png"
                                        radius:20
                            MDBoxLayout:
                                orientation:
                                    "vertical"
                                md_bg_color: (56/255,40/255,81/255,1)
                                size_hint_y: 0.1
                                size_hint_x: 1
                                pos_hint:{"top":0.88}
                                radius: 30
                                TwoLineAvatarListItem:
                                    text: "LEVEL 100 1301 V1"
                                    secondary_text:"Questions"
                                    ImageLeftWidget:
                                        source:"icon.png"
                                        radius:20
                                        
                            MDBoxLayout:
                                orientation:
                                    "vertical"
                                md_bg_color: (56/255,40/255,81/255,1)
                                size_hint_y: 0.1
                                size_hint_x: 1
                                pos_hint:{"top":0.34}
                                radius: 30
                                TwoLineAvatarListItem:
                                    text: "LEVEL 100 1301 V1"
                                    secondary_text:"Questions"
                                    ImageLeftWidget:
                                        source:"icon.png"
                                        radius:20
                                        
                            MDBoxLayout:
                                orientation:
                                    "vertical"
                                md_bg_color: (56/255,40/255,81/255,1)
                                size_hint_y: 0.1
                                size_hint_x: 1
                                pos_hint:{"top":0.22}
                                radius: 30
                                TwoLineAvatarListItem:
                                    text: "LEVEL 100 1301 V1"
                                    secondary_text:"Questions"
                                    ImageLeftWidget:
                                        source:"icon.png"
                                        radius:20         
                            MDBoxLayout:
                                orientation:
                                    "vertical"
                                md_bg_color: (56/255,40/255,81/255,1)
                                size_hint_y: 0.1
                                size_hint_x: 1
                                pos_hint:{"top":0.1}
                                radius: 30
                                TwoLineAvatarListItem
                                    text: "LEVEL 100 1301 V1"
                                    secondary_text:"Questions"
                                    ImageLeftWidget:
                                        source:"icon.png"
                                        radius:20            
                                
                                
                                
                                
                            MDFloatLayout:
                                md_bg_color: (56/255,40/255,81/255,1)
                                size_hint_x: 1
                                size_hint_y: 0.35
                                pos_hint:{"top":0.75}
                                radius: 20
                                padding:("10dp","10dp","10dp","10dp")
                                MDFloatLayout:
                                    #orientation:
                                    padding:("10dp","0dp","0dp","10dp")
                                    radius:30
                                    md_bg_color: (56/255,40/255,81/255,1)
                                    pos_hint:{"top":1}
                                    size_hint_y: 0.2
                                    size_hint_x: 1
                                    MDTextButton:
                                        text: "More"
                                        color:"blue"
                                        pos_hint:{"top":0.8,"x":0.8}
                                       
                                        
                                        
                                    MDLabel:
                                        text: "Topics"
                                        color: (1,1,1,1)
                                        pos_hint:{"top":1.1,"x":0.15}
                                        bold:"true"
                                    MDIcon:
                                        
                                        icon:"book-arrow-down"
                                        pos_hint:{"center_x":0.1, "center_y":0.6}
                                        
                                  
                                 
                                    
                                 
                                MDScrollView:
                                    size_hint_x: 1.1
                                    do_scroll_y: True
                                    do_scroll_x: True
                                    size_hint_y: 0.8
                                    #md_bg_color: (1,1,1,1)
                                    pos_hint:{"top":0.88}
                                    width: 100
                                    MDGridLayout:
                                        rows: 2
                                        #cols:2
                                        #do_scroll_y: True
                                        #do_scroll_x: True
                                        #md_bg_color:(1,2,2,3)
                                        size_hint_x: 1.1
                                        size_hint_y: 1
                                        #pos_hint:{"top": }
                                        width:self.minimum_width
                                        height: self.minimum_height
                                        spacing: "20dp", "20dp"
                                        width: 0
                                        padding: "20dp"
                                        radius:20
                                        
                                        MDCard:
                                            text:"eubiu"
                                            size_hint: 1,1
                                            md_bg_color: (0,1,1,0.3)
                                        MDCard:
                                            text:"eubiu"
                                            size_hint: 1,1
                                            md_bg_color: (0,1,1,0.3)
                                        MDCard:
                                            text:"eubiu"
                                            size_hint: 1,1
                                            md_bg_color: (0,1,1,0.3)
                                        MDCard:
                                            text:"eubiu"
                                            size_hint: 1,1
                                            md_bg_color: (0,1,1,0.3)
                                        MDCard:
                                            text:"eubiu"
                                            size_hint: 1,1
                                            md_bg_color: (0,1,1,0.3)
                                        MDCard:
                                            text:"eubiu"
                                            size_hint: 1,1
                                            md_bg_color: (0,1,1,0.3)
        MDBottomNavigationItem:
            name:"nav 2"
            text:"Books"
            icon:"book-education"
            MDLabel:
                text:"hhgjgj"                            
                                                                                        
        MDBottomNavigationItem:
            name:"nav 3"
            text:"Questions"
            icon:"lightbulb-question"
            MDLabel:
                text:"hhgjgj"
        MDBottomNavigationItem:
            name:"nav 4"
            text:"Behind"
            icon:"key-variant"
            MDLabel:
                text:"hhgjgj"
        MDBottomNavigationItem:
            name:"nav 5"
            text:"About"
            icon:"web"
            MDLabel:
                text:"uhug"    
                          
                                
                                        
                                                                                          
                         
                                
                
                
                 
                                    
                                       
                            
                                
                                
                                
                                
                        
                                
                                
                        
                
               
    MDNavigationDrawer:
        id: nav_drawer
        md_bg_color: (56/255,40/255,81/255,1)
        size_hint:0.8,1
        MDBoxLayout:
            orientation:
                "vertical"                     
               
            
                    
            
<Screen3>:
    name:"p" 
    
    
    
    
    
    
<Screen4>:
    name:"f"           
            
          
           
                     

                    
#size_hint: 
#padding:("20dp","20dp","20dp","20dp")
#pos_hint: {"top":0.9}
        
       
            

            
            
            
            
            
            
            
            
            
"""


class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class Screen1(Screen):
    pass


class Screen2(Screen):
    pass


class Screen3(Screen):
    pass


class Screen4(Screen):
    pass


class Screen5(Screen):
    pass


class Screen6(Screen):
    pass


class Screen7(Screen):
    pass


class Screen8(Screen):
    pass


screenmanager = MDScreenManager()
screenmanager.add_widget(Screen1(name="page 1"))
screenmanager.add_widget(Screen2(name="page 2"))
screenmanager.add_widget(Screen3(name="p"))
screenmanager.add_widget(Screen4(name="f"))




class Level_One_v1(MDApp):

    # lobal  screen
    # screen = Screen()

    def build(self):
        screen = Screen()
        self.icon = "icon.png"

        self.screens = (Builder.load_string(screen_helper))
        screen.add_widget(self.screens)

        return screen

    def on_start(self):
        Clock.schedule_once(self.page, 3)

    def page(self, *args):
        self.screens.current = "page 2"



if __name__ == "__main__":
    Level_One_v1().run()
