screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'Menu'
    MDRectangleFlatButton:
        text:'Profile'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: root.manager.current = 'Profile'

    MDRectangleFlatButton:
        text:'Upload'
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press: root.manager.current = 'Upload'

<ProfileScreen>
    name: 'Profile'
    MDLabel:
        text: 'Welcome Hasira'
        halign: 'center'
    MDRectangleFlatButton:
        text:'Back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'Menu'

<UploadScreen>
    name: 'Upload'
    MDLabel:
        text: 'Upload Your Photo!'
        halign: 'center'
    MDRectangleFlatButton:
        text:'Back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'Menu'
"""
