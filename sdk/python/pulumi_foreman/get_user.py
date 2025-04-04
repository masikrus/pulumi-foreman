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
    'GetUserResult',
    'AwaitableGetUserResult',
    'get_user',
    'get_user_output',
]

@pulumi.output_type
class GetUserResult:
    """
    A collection of values returned by getUser.
    """
    def __init__(__self__, admin=None, auth_source_id=None, default_location_id=None, default_organization_id=None, description=None, firstname=None, id=None, lastname=None, locale=None, location_ids=None, login=None, mail=None, organization_ids=None, password=None):
        if admin and not isinstance(admin, bool):
            raise TypeError("Expected argument 'admin' to be a bool")
        pulumi.set(__self__, "admin", admin)
        if auth_source_id and not isinstance(auth_source_id, int):
            raise TypeError("Expected argument 'auth_source_id' to be a int")
        pulumi.set(__self__, "auth_source_id", auth_source_id)
        if default_location_id and not isinstance(default_location_id, int):
            raise TypeError("Expected argument 'default_location_id' to be a int")
        pulumi.set(__self__, "default_location_id", default_location_id)
        if default_organization_id and not isinstance(default_organization_id, int):
            raise TypeError("Expected argument 'default_organization_id' to be a int")
        pulumi.set(__self__, "default_organization_id", default_organization_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if firstname and not isinstance(firstname, str):
            raise TypeError("Expected argument 'firstname' to be a str")
        pulumi.set(__self__, "firstname", firstname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lastname and not isinstance(lastname, str):
            raise TypeError("Expected argument 'lastname' to be a str")
        pulumi.set(__self__, "lastname", lastname)
        if locale and not isinstance(locale, str):
            raise TypeError("Expected argument 'locale' to be a str")
        pulumi.set(__self__, "locale", locale)
        if location_ids and not isinstance(location_ids, list):
            raise TypeError("Expected argument 'location_ids' to be a list")
        pulumi.set(__self__, "location_ids", location_ids)
        if login and not isinstance(login, str):
            raise TypeError("Expected argument 'login' to be a str")
        pulumi.set(__self__, "login", login)
        if mail and not isinstance(mail, str):
            raise TypeError("Expected argument 'mail' to be a str")
        pulumi.set(__self__, "mail", mail)
        if organization_ids and not isinstance(organization_ids, list):
            raise TypeError("Expected argument 'organization_ids' to be a list")
        pulumi.set(__self__, "organization_ids", organization_ids)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter
    def admin(self) -> bool:
        return pulumi.get(self, "admin")

    @property
    @pulumi.getter(name="authSourceId")
    def auth_source_id(self) -> int:
        return pulumi.get(self, "auth_source_id")

    @property
    @pulumi.getter(name="defaultLocationId")
    def default_location_id(self) -> int:
        return pulumi.get(self, "default_location_id")

    @property
    @pulumi.getter(name="defaultOrganizationId")
    def default_organization_id(self) -> int:
        return pulumi.get(self, "default_organization_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def firstname(self) -> Optional[str]:
        return pulumi.get(self, "firstname")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def lastname(self) -> Optional[str]:
        return pulumi.get(self, "lastname")

    @property
    @pulumi.getter
    def locale(self) -> str:
        return pulumi.get(self, "locale")

    @property
    @pulumi.getter(name="locationIds")
    def location_ids(self) -> Sequence[int]:
        return pulumi.get(self, "location_ids")

    @property
    @pulumi.getter
    def login(self) -> Optional[str]:
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def mail(self) -> Optional[str]:
        return pulumi.get(self, "mail")

    @property
    @pulumi.getter(name="organizationIds")
    def organization_ids(self) -> Sequence[int]:
        return pulumi.get(self, "organization_ids")

    @property
    @pulumi.getter
    def password(self) -> str:
        return pulumi.get(self, "password")


class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            admin=self.admin,
            auth_source_id=self.auth_source_id,
            default_location_id=self.default_location_id,
            default_organization_id=self.default_organization_id,
            description=self.description,
            firstname=self.firstname,
            id=self.id,
            lastname=self.lastname,
            locale=self.locale,
            location_ids=self.location_ids,
            login=self.login,
            mail=self.mail,
            organization_ids=self.organization_ids,
            password=self.password)


def get_user(description: Optional[str] = None,
             firstname: Optional[str] = None,
             lastname: Optional[str] = None,
             login: Optional[str] = None,
             mail: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['firstname'] = firstname
    __args__['lastname'] = lastname
    __args__['login'] = login
    __args__['mail'] = mail
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('foreman:index/getUser:getUser', __args__, opts=opts, typ=GetUserResult).value

    return AwaitableGetUserResult(
        admin=pulumi.get(__ret__, 'admin'),
        auth_source_id=pulumi.get(__ret__, 'auth_source_id'),
        default_location_id=pulumi.get(__ret__, 'default_location_id'),
        default_organization_id=pulumi.get(__ret__, 'default_organization_id'),
        description=pulumi.get(__ret__, 'description'),
        firstname=pulumi.get(__ret__, 'firstname'),
        id=pulumi.get(__ret__, 'id'),
        lastname=pulumi.get(__ret__, 'lastname'),
        locale=pulumi.get(__ret__, 'locale'),
        location_ids=pulumi.get(__ret__, 'location_ids'),
        login=pulumi.get(__ret__, 'login'),
        mail=pulumi.get(__ret__, 'mail'),
        organization_ids=pulumi.get(__ret__, 'organization_ids'),
        password=pulumi.get(__ret__, 'password'))
def get_user_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                    firstname: Optional[pulumi.Input[Optional[str]]] = None,
                    lastname: Optional[pulumi.Input[Optional[str]]] = None,
                    login: Optional[pulumi.Input[Optional[str]]] = None,
                    mail: Optional[pulumi.Input[Optional[str]]] = None,
                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetUserResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['firstname'] = firstname
    __args__['lastname'] = lastname
    __args__['login'] = login
    __args__['mail'] = mail
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('foreman:index/getUser:getUser', __args__, opts=opts, typ=GetUserResult)
    return __ret__.apply(lambda __response__: GetUserResult(
        admin=pulumi.get(__response__, 'admin'),
        auth_source_id=pulumi.get(__response__, 'auth_source_id'),
        default_location_id=pulumi.get(__response__, 'default_location_id'),
        default_organization_id=pulumi.get(__response__, 'default_organization_id'),
        description=pulumi.get(__response__, 'description'),
        firstname=pulumi.get(__response__, 'firstname'),
        id=pulumi.get(__response__, 'id'),
        lastname=pulumi.get(__response__, 'lastname'),
        locale=pulumi.get(__response__, 'locale'),
        location_ids=pulumi.get(__response__, 'location_ids'),
        login=pulumi.get(__response__, 'login'),
        mail=pulumi.get(__response__, 'mail'),
        organization_ids=pulumi.get(__response__, 'organization_ids'),
        password=pulumi.get(__response__, 'password')))
