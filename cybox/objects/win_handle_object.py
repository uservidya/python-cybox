import common_methods
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_handle_object_1_3 as win_handle_binding
from cybox.common.baseobjectattribute import baseobjectattribute

class win_handle_object:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, handle_attributes):
        """Create the Win Handle Object object representation from an input dictionary"""
        handle_obj = cybox_win_handle_object.WindowsHandleObjectType()
        handle_obj.set_anyAttributes_({'xsi:type' : 'WinHandleObj:WindowsHandleObjectType'})
        
        for key, value in handle_attributes.items():
            if key == 'id' and common_methods.test_value(value):
                handle_obj.set_ID(baseobjectattribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInt'), value))
            if key == 'name' and common_methods.test_value(value):
                handle_obj.set_Name(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'type' and common_methods.test_value(value):
                handle_obj.set_Type(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'object_address' and common_methods.test_value(value):
                handle_obj.set_Object_Address(baseobjectattribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            if key == 'access_mask' and common_methods.test_value(value):
                handle_obj.set_Access_Mask(baseobjectattribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            if key == 'pointer_count' and common_methods.test_value(value):
                handle_obj.set_Pointer_Count(baseobjectattribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
                
        return handle_obj
    
    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for a Win Handle Object object"""    
        if defined_object.get_ID() is not None:
            defined_object_dict["id"] = baseobjectattribute.dict_from_object(defined_object.get_ID())
        if defined_object.get_Type() is not None:
            defined_object_dict["type"] = baseobjectattribute.dict_from_object(defined_object.get_Type())
        if defined_object.get_Name() is not None:
            defined_object_dict["name"] = baseobjectattribute.dict_from_object(defined_object.get_Name())
        if defined_object.get_Object_Address() is not None:
            defined_object_dict["object_address"] = baseobjectattribute.dict_from_object(defined_object.get_Object_Address())
        if defined_object.get_Access_Mask() is not None:
            defined_object_dict["access_mask"] = baseobjectattribute.dict_from_object(defined_object.get_Access_Mask())
        if defined_object.get_Pointer_Count() is not None:
            defined_object_dict["type"] = baseobjectattribute.dict_from_object(defined_object.get_Pointer_Count())
            
        return defined_object_dict


    @classmethod
    def create_list_from_dict(cls, handle_list):
        """Create a Win Handle List Object from an input handle list"""
        handle_list_object = win_handle_binding.WindowsHandleListType()
        for win_handle_dict in handle_list:
            handle_object = cls.object_from_dict(win_handle_dict)
            if handle_object.hasContent_():
                handle_list_object.add_Handle(handle_object)

        return handle_list_object

    @classmethod
    def parse_list_into_dict(cls, list_object):
        """Parse and return a dictionary for a Win Handle List object"""
        handle_list = []
        for win_handle in list_object.get_Handle():
            handle_list.append(cls.dict_from_object(win_handle))
            
        return handle_list
