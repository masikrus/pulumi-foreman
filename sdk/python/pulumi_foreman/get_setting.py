# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = [
    'GetSettingResult',
    'AwaitableGetSettingResult',
    'get_setting',
    'get_setting_output',
]

@pulumi.output_type
class GetSettingResult:
    """
    A collection of values returned by getSetting.
    """
    def __init__(__self__, category_name=None, default=None, description=None, id=None, name=None, readonly=None, settings_type=None, value=None):
        if category_name and not isinstance(category_name, str):
            raise TypeError("Expected argument 'category_name' to be a str")
        pulumi.set(__self__, "category_name", category_name)
        if default and not isinstance(default, str):
            raise TypeError("Expected argument 'default' to be a str")
        pulumi.set(__self__, "default", default)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if readonly and not isinstance(readonly, bool):
            raise TypeError("Expected argument 'readonly' to be a bool")
        pulumi.set(__self__, "readonly", readonly)
        if settings_type and not isinstance(settings_type, str):
            raise TypeError("Expected argument 'settings_type' to be a str")
        pulumi.set(__self__, "settings_type", settings_type)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="categoryName")
    def category_name(self) -> str:
        return pulumi.get(self, "category_name")

    @property
    @pulumi.getter
    def default(self) -> str:
        return pulumi.get(self, "default")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def readonly(self) -> bool:
        return pulumi.get(self, "readonly")

    @property
    @pulumi.getter(name="settingsType")
    def settings_type(self) -> str:
        return pulumi.get(self, "settings_type")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


class AwaitableGetSettingResult(GetSettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSettingResult(
            category_name=self.category_name,
            default=self.default,
            description=self.description,
            id=self.id,
            name=self.name,
            readonly=self.readonly,
            settings_type=self.settings_type,
            value=self.value)


def get_setting(name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSettingResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('foreman:index/getSetting:getSetting', __args__, opts=opts, typ=GetSettingResult).value

    return AwaitableGetSettingResult(
        category_name=pulumi.get(__ret__, 'category_name'),
        default=pulumi.get(__ret__, 'default'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        readonly=pulumi.get(__ret__, 'readonly'),
        settings_type=pulumi.get(__ret__, 'settings_type'),
        value=pulumi.get(__ret__, 'value'))
def get_setting_output(name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetSettingResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('foreman:index/getSetting:getSetting', __args__, opts=opts, typ=GetSettingResult)
    return __ret__.apply(lambda __response__: GetSettingResult(
        category_name=pulumi.get(__response__, 'category_name'),
        default=pulumi.get(__response__, 'default'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        readonly=pulumi.get(__response__, 'readonly'),
        settings_type=pulumi.get(__response__, 'settings_type'),
        value=pulumi.get(__response__, 'value')))
