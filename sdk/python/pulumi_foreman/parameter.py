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

__all__ = ['ParameterArgs', 'Parameter']

@pulumi.input_type
class ParameterArgs:
    def __init__(__self__, *,
                 value: pulumi.Input[str],
                 domain_id: Optional[pulumi.Input[int]] = None,
                 host_id: Optional[pulumi.Input[int]] = None,
                 hostgroup_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operatingsystem_id: Optional[pulumi.Input[int]] = None,
                 subnet_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Parameter resource.
        :param pulumi.Input[int] domain_id: ID of the domain to assign this parameter to
        :param pulumi.Input[int] host_id: ID of the host to assign this parameter to
        :param pulumi.Input[int] hostgroup_id: ID of the host group to assign this parameter to
        :param pulumi.Input[int] operatingsystem_id: ID of the operating system to assign this parameter to
        :param pulumi.Input[int] subnet_id: ID of the subnet to assign this parameter to
        """
        pulumi.set(__self__, "value", value)
        if domain_id is not None:
            pulumi.set(__self__, "domain_id", domain_id)
        if host_id is not None:
            pulumi.set(__self__, "host_id", host_id)
        if hostgroup_id is not None:
            pulumi.set(__self__, "hostgroup_id", hostgroup_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if operatingsystem_id is not None:
            pulumi.set(__self__, "operatingsystem_id", operatingsystem_id)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the domain to assign this parameter to
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "domain_id", value)

    @property
    @pulumi.getter(name="hostId")
    def host_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the host to assign this parameter to
        """
        return pulumi.get(self, "host_id")

    @host_id.setter
    def host_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "host_id", value)

    @property
    @pulumi.getter(name="hostgroupId")
    def hostgroup_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the host group to assign this parameter to
        """
        return pulumi.get(self, "hostgroup_id")

    @hostgroup_id.setter
    def hostgroup_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "hostgroup_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="operatingsystemId")
    def operatingsystem_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the operating system to assign this parameter to
        """
        return pulumi.get(self, "operatingsystem_id")

    @operatingsystem_id.setter
    def operatingsystem_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "operatingsystem_id", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the subnet to assign this parameter to
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "subnet_id", value)


@pulumi.input_type
class _ParameterState:
    def __init__(__self__, *,
                 __meta_: Optional[pulumi.Input[bool]] = None,
                 domain_id: Optional[pulumi.Input[int]] = None,
                 host_id: Optional[pulumi.Input[int]] = None,
                 hostgroup_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operatingsystem_id: Optional[pulumi.Input[int]] = None,
                 subnet_id: Optional[pulumi.Input[int]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Parameter resources.
        :param pulumi.Input[bool] __meta_: @SUMMARY Foreman representation of parameter. Parameters serve as an identification string that defines autonomy,
               authority, or control for a portion of a network.
        :param pulumi.Input[int] domain_id: ID of the domain to assign this parameter to
        :param pulumi.Input[int] host_id: ID of the host to assign this parameter to
        :param pulumi.Input[int] hostgroup_id: ID of the host group to assign this parameter to
        :param pulumi.Input[int] operatingsystem_id: ID of the operating system to assign this parameter to
        :param pulumi.Input[int] subnet_id: ID of the subnet to assign this parameter to
        """
        if __meta_ is not None:
            pulumi.set(__self__, "__meta_", __meta_)
        if domain_id is not None:
            pulumi.set(__self__, "domain_id", domain_id)
        if host_id is not None:
            pulumi.set(__self__, "host_id", host_id)
        if hostgroup_id is not None:
            pulumi.set(__self__, "hostgroup_id", hostgroup_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if operatingsystem_id is not None:
            pulumi.set(__self__, "operatingsystem_id", operatingsystem_id)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def __meta_(self) -> Optional[pulumi.Input[bool]]:
        """
        @SUMMARY Foreman representation of parameter. Parameters serve as an identification string that defines autonomy,
        authority, or control for a portion of a network.
        """
        return pulumi.get(self, "__meta_")

    @__meta_.setter
    def __meta_(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "__meta_", value)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the domain to assign this parameter to
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "domain_id", value)

    @property
    @pulumi.getter(name="hostId")
    def host_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the host to assign this parameter to
        """
        return pulumi.get(self, "host_id")

    @host_id.setter
    def host_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "host_id", value)

    @property
    @pulumi.getter(name="hostgroupId")
    def hostgroup_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the host group to assign this parameter to
        """
        return pulumi.get(self, "hostgroup_id")

    @hostgroup_id.setter
    def hostgroup_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "hostgroup_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="operatingsystemId")
    def operatingsystem_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the operating system to assign this parameter to
        """
        return pulumi.get(self, "operatingsystem_id")

    @operatingsystem_id.setter
    def operatingsystem_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "operatingsystem_id", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the subnet to assign this parameter to
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class Parameter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_id: Optional[pulumi.Input[int]] = None,
                 host_id: Optional[pulumi.Input[int]] = None,
                 hostgroup_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operatingsystem_id: Optional[pulumi.Input[int]] = None,
                 subnet_id: Optional[pulumi.Input[int]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Parameter resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] domain_id: ID of the domain to assign this parameter to
        :param pulumi.Input[int] host_id: ID of the host to assign this parameter to
        :param pulumi.Input[int] hostgroup_id: ID of the host group to assign this parameter to
        :param pulumi.Input[int] operatingsystem_id: ID of the operating system to assign this parameter to
        :param pulumi.Input[int] subnet_id: ID of the subnet to assign this parameter to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ParameterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Parameter resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ParameterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ParameterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_id: Optional[pulumi.Input[int]] = None,
                 host_id: Optional[pulumi.Input[int]] = None,
                 hostgroup_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operatingsystem_id: Optional[pulumi.Input[int]] = None,
                 subnet_id: Optional[pulumi.Input[int]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ParameterArgs.__new__(ParameterArgs)

            __props__.__dict__["domain_id"] = domain_id
            __props__.__dict__["host_id"] = host_id
            __props__.__dict__["hostgroup_id"] = hostgroup_id
            __props__.__dict__["name"] = name
            __props__.__dict__["operatingsystem_id"] = operatingsystem_id
            __props__.__dict__["subnet_id"] = subnet_id
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
            __props__.__dict__["__meta_"] = None
        super(Parameter, __self__).__init__(
            'foreman:index/parameter:Parameter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            __meta_: Optional[pulumi.Input[bool]] = None,
            domain_id: Optional[pulumi.Input[int]] = None,
            host_id: Optional[pulumi.Input[int]] = None,
            hostgroup_id: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            operatingsystem_id: Optional[pulumi.Input[int]] = None,
            subnet_id: Optional[pulumi.Input[int]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'Parameter':
        """
        Get an existing Parameter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] __meta_: @SUMMARY Foreman representation of parameter. Parameters serve as an identification string that defines autonomy,
               authority, or control for a portion of a network.
        :param pulumi.Input[int] domain_id: ID of the domain to assign this parameter to
        :param pulumi.Input[int] host_id: ID of the host to assign this parameter to
        :param pulumi.Input[int] hostgroup_id: ID of the host group to assign this parameter to
        :param pulumi.Input[int] operatingsystem_id: ID of the operating system to assign this parameter to
        :param pulumi.Input[int] subnet_id: ID of the subnet to assign this parameter to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ParameterState.__new__(_ParameterState)

        __props__.__dict__["__meta_"] = __meta_
        __props__.__dict__["domain_id"] = domain_id
        __props__.__dict__["host_id"] = host_id
        __props__.__dict__["hostgroup_id"] = hostgroup_id
        __props__.__dict__["name"] = name
        __props__.__dict__["operatingsystem_id"] = operatingsystem_id
        __props__.__dict__["subnet_id"] = subnet_id
        __props__.__dict__["value"] = value
        return Parameter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def __meta_(self) -> pulumi.Output[bool]:
        """
        @SUMMARY Foreman representation of parameter. Parameters serve as an identification string that defines autonomy,
        authority, or control for a portion of a network.
        """
        return pulumi.get(self, "__meta_")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[Optional[int]]:
        """
        ID of the domain to assign this parameter to
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="hostId")
    def host_id(self) -> pulumi.Output[Optional[int]]:
        """
        ID of the host to assign this parameter to
        """
        return pulumi.get(self, "host_id")

    @property
    @pulumi.getter(name="hostgroupId")
    def hostgroup_id(self) -> pulumi.Output[Optional[int]]:
        """
        ID of the host group to assign this parameter to
        """
        return pulumi.get(self, "hostgroup_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operatingsystemId")
    def operatingsystem_id(self) -> pulumi.Output[Optional[int]]:
        """
        ID of the operating system to assign this parameter to
        """
        return pulumi.get(self, "operatingsystem_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[int]]:
        """
        ID of the subnet to assign this parameter to
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        return pulumi.get(self, "value")

