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
    'GetKatelloLifecycleEnvironmentResult',
    'AwaitableGetKatelloLifecycleEnvironmentResult',
    'get_katello_lifecycle_environment',
    'get_katello_lifecycle_environment_output',
]

@pulumi.output_type
class GetKatelloLifecycleEnvironmentResult:
    """
    A collection of values returned by getKatelloLifecycleEnvironment.
    """
    def __init__(__self__, description=None, id=None, label=None, library=None, name=None, organization_id=None, prior_id=None, successor_id=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if library and not isinstance(library, bool):
            raise TypeError("Expected argument 'library' to be a bool")
        pulumi.set(__self__, "library", library)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if organization_id and not isinstance(organization_id, int):
            raise TypeError("Expected argument 'organization_id' to be a int")
        pulumi.set(__self__, "organization_id", organization_id)
        if prior_id and not isinstance(prior_id, int):
            raise TypeError("Expected argument 'prior_id' to be a int")
        pulumi.set(__self__, "prior_id", prior_id)
        if successor_id and not isinstance(successor_id, int):
            raise TypeError("Expected argument 'successor_id' to be a int")
        pulumi.set(__self__, "successor_id", successor_id)

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
    def label(self) -> str:
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def library(self) -> bool:
        return pulumi.get(self, "library")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> int:
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="priorId")
    def prior_id(self) -> int:
        return pulumi.get(self, "prior_id")

    @property
    @pulumi.getter(name="successorId")
    def successor_id(self) -> int:
        return pulumi.get(self, "successor_id")


class AwaitableGetKatelloLifecycleEnvironmentResult(GetKatelloLifecycleEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKatelloLifecycleEnvironmentResult(
            description=self.description,
            id=self.id,
            label=self.label,
            library=self.library,
            name=self.name,
            organization_id=self.organization_id,
            prior_id=self.prior_id,
            successor_id=self.successor_id)


def get_katello_lifecycle_environment(name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKatelloLifecycleEnvironmentResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('foreman:index/getKatelloLifecycleEnvironment:getKatelloLifecycleEnvironment', __args__, opts=opts, typ=GetKatelloLifecycleEnvironmentResult).value

    return AwaitableGetKatelloLifecycleEnvironmentResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        label=pulumi.get(__ret__, 'label'),
        library=pulumi.get(__ret__, 'library'),
        name=pulumi.get(__ret__, 'name'),
        organization_id=pulumi.get(__ret__, 'organization_id'),
        prior_id=pulumi.get(__ret__, 'prior_id'),
        successor_id=pulumi.get(__ret__, 'successor_id'))
def get_katello_lifecycle_environment_output(name: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetKatelloLifecycleEnvironmentResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('foreman:index/getKatelloLifecycleEnvironment:getKatelloLifecycleEnvironment', __args__, opts=opts, typ=GetKatelloLifecycleEnvironmentResult)
    return __ret__.apply(lambda __response__: GetKatelloLifecycleEnvironmentResult(
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        label=pulumi.get(__response__, 'label'),
        library=pulumi.get(__response__, 'library'),
        name=pulumi.get(__response__, 'name'),
        organization_id=pulumi.get(__response__, 'organization_id'),
        prior_id=pulumi.get(__response__, 'prior_id'),
        successor_id=pulumi.get(__response__, 'successor_id')))
