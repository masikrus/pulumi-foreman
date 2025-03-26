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
    'GetKatelloSyncPlanResult',
    'AwaitableGetKatelloSyncPlanResult',
    'get_katello_sync_plan',
    'get_katello_sync_plan_output',
]

@pulumi.output_type
class GetKatelloSyncPlanResult:
    """
    A collection of values returned by getKatelloSyncPlan.
    """
    def __init__(__self__, cron_expression=None, description=None, enabled=None, id=None, interval=None, name=None, sync_date=None):
        if cron_expression and not isinstance(cron_expression, str):
            raise TypeError("Expected argument 'cron_expression' to be a str")
        pulumi.set(__self__, "cron_expression", cron_expression)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interval and not isinstance(interval, str):
            raise TypeError("Expected argument 'interval' to be a str")
        pulumi.set(__self__, "interval", interval)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sync_date and not isinstance(sync_date, str):
            raise TypeError("Expected argument 'sync_date' to be a str")
        pulumi.set(__self__, "sync_date", sync_date)

    @property
    @pulumi.getter(name="cronExpression")
    def cron_expression(self) -> str:
        return pulumi.get(self, "cron_expression")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def interval(self) -> str:
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="syncDate")
    def sync_date(self) -> str:
        return pulumi.get(self, "sync_date")


class AwaitableGetKatelloSyncPlanResult(GetKatelloSyncPlanResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKatelloSyncPlanResult(
            cron_expression=self.cron_expression,
            description=self.description,
            enabled=self.enabled,
            id=self.id,
            interval=self.interval,
            name=self.name,
            sync_date=self.sync_date)


def get_katello_sync_plan(name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKatelloSyncPlanResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('foreman:index/getKatelloSyncPlan:getKatelloSyncPlan', __args__, opts=opts, typ=GetKatelloSyncPlanResult).value

    return AwaitableGetKatelloSyncPlanResult(
        cron_expression=pulumi.get(__ret__, 'cron_expression'),
        description=pulumi.get(__ret__, 'description'),
        enabled=pulumi.get(__ret__, 'enabled'),
        id=pulumi.get(__ret__, 'id'),
        interval=pulumi.get(__ret__, 'interval'),
        name=pulumi.get(__ret__, 'name'),
        sync_date=pulumi.get(__ret__, 'sync_date'))
def get_katello_sync_plan_output(name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetKatelloSyncPlanResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('foreman:index/getKatelloSyncPlan:getKatelloSyncPlan', __args__, opts=opts, typ=GetKatelloSyncPlanResult)
    return __ret__.apply(lambda __response__: GetKatelloSyncPlanResult(
        cron_expression=pulumi.get(__response__, 'cron_expression'),
        description=pulumi.get(__response__, 'description'),
        enabled=pulumi.get(__response__, 'enabled'),
        id=pulumi.get(__response__, 'id'),
        interval=pulumi.get(__response__, 'interval'),
        name=pulumi.get(__response__, 'name'),
        sync_date=pulumi.get(__response__, 'sync_date')))
