"""
This class models the Qxf2.com header as a Page Object.
The header consists of the Qxf2 logo, Qxf2 tag-line and the hamburger menu
Since the hanburger menu is complex, we will model it as a separate object  
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class {{cookiecutter.page_object_class_name}}():
    "Page Object for the {{cookiecutter.page_object_class_name}} class"

    #locators
    
    @Wrapit._exceptionHandler
    def get_URL(self):
        "Check current URL"
        return self.get_current_url()

    

    
