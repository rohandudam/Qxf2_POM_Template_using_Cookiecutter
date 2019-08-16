"""
PageFactory uses the factory design pattern. 
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Tutorial main page
2. Tutorial redirect page
3. Contact Page
4. Bitcoin main page
5. Bitcoin price page
"""

from page_objects.{{cookiecutter.page_object_name}} import {{cookiecutter.page_object_class_name}}


class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url='{{cookiecutter.project_url}}',trailing_slash_flag=True):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name == "main page":
            test_obj = {{cookiecutter.page_object_class_name}}(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        return test_obj

    get_page_object = staticmethod(get_page_object)