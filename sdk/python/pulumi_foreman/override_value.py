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

__all__ = ['OverrideValueArgs', 'OverrideValue']

@pulumi.input_type
class OverrideValueArgs:
    def __init__(__self__, *,
                 match: pulumi.Input[Mapping[str, pulumi.Input[str]]],
                 smart_class_parameter_id: pulumi.Input[int],
                 value: pulumi.Input[str],
                 omit: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a OverrideValue resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] match: A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
               `domain` or `os`@EXAMPLE { type = "hostgroup" value = "example_group" }
        :param pulumi.Input[int] smart_class_parameter_id: ID of the smart class parameter to override.@EXAMPLE 1
        :param pulumi.Input[str] value: Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
        :param pulumi.Input[bool] omit: When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
               false
        """
        pulumi.set(__self__, "match", match)
        pulumi.set(__self__, "smart_class_parameter_id", smart_class_parameter_id)
        pulumi.set(__self__, "value", value)
        if omit is not None:
            pulumi.set(__self__, "omit", omit)

    @property
    @pulumi.getter
    def match(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
        `domain` or `os`@EXAMPLE { type = "hostgroup" value = "example_group" }
        """
        return pulumi.get(self, "match")

    @match.setter
    def match(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "match", value)

    @property
    @pulumi.getter(name="smartClassParameterId")
    def smart_class_parameter_id(self) -> pulumi.Input[int]:
        """
        ID of the smart class parameter to override.@EXAMPLE 1
        """
        return pulumi.get(self, "smart_class_parameter_id")

    @smart_class_parameter_id.setter
    def smart_class_parameter_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "smart_class_parameter_id", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter
    def omit(self) -> Optional[pulumi.Input[bool]]:
        """
        When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
        false
        """
        return pulumi.get(self, "omit")

    @omit.setter
    def omit(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "omit", value)


@pulumi.input_type
class _OverrideValueState:
    def __init__(__self__, *,
                 __meta_: Optional[pulumi.Input[bool]] = None,
                 match: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 omit: Optional[pulumi.Input[bool]] = None,
                 smart_class_parameter_id: Optional[pulumi.Input[int]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OverrideValue resources.
        :param pulumi.Input[bool] __meta_: @SUMMARY Smart class parameter override value.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] match: A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
               `domain` or `os`@EXAMPLE { type = "hostgroup" value = "example_group" }
        :param pulumi.Input[bool] omit: When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
               false
        :param pulumi.Input[int] smart_class_parameter_id: ID of the smart class parameter to override.@EXAMPLE 1
        :param pulumi.Input[str] value: Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
        """
        if __meta_ is not None:
            pulumi.set(__self__, "__meta_", __meta_)
        if match is not None:
            pulumi.set(__self__, "match", match)
        if omit is not None:
            pulumi.set(__self__, "omit", omit)
        if smart_class_parameter_id is not None:
            pulumi.set(__self__, "smart_class_parameter_id", smart_class_parameter_id)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def __meta_(self) -> Optional[pulumi.Input[bool]]:
        """
        @SUMMARY Smart class parameter override value.
        """
        return pulumi.get(self, "__meta_")

    @__meta_.setter
    def __meta_(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "__meta_", value)

    @property
    @pulumi.getter
    def match(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
        `domain` or `os`@EXAMPLE { type = "hostgroup" value = "example_group" }
        """
        return pulumi.get(self, "match")

    @match.setter
    def match(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "match", value)

    @property
    @pulumi.getter
    def omit(self) -> Optional[pulumi.Input[bool]]:
        """
        When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
        false
        """
        return pulumi.get(self, "omit")

    @omit.setter
    def omit(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "omit", value)

    @property
    @pulumi.getter(name="smartClassParameterId")
    def smart_class_parameter_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the smart class parameter to override.@EXAMPLE 1
        """
        return pulumi.get(self, "smart_class_parameter_id")

    @smart_class_parameter_id.setter
    def smart_class_parameter_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "smart_class_parameter_id", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class OverrideValue(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 match: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 omit: Optional[pulumi.Input[bool]] = None,
                 smart_class_parameter_id: Optional[pulumi.Input[int]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a OverrideValue resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] match: A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
               `domain` or `os`@EXAMPLE { type = "hostgroup" value = "example_group" }
        :param pulumi.Input[bool] omit: When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
               false
        :param pulumi.Input[int] smart_class_parameter_id: ID of the smart class parameter to override.@EXAMPLE 1
        :param pulumi.Input[str] value: Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OverrideValueArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a OverrideValue resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param OverrideValueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OverrideValueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 match: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 omit: Optional[pulumi.Input[bool]] = None,
                 smart_class_parameter_id: Optional[pulumi.Input[int]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OverrideValueArgs.__new__(OverrideValueArgs)

            if match is None and not opts.urn:
                raise TypeError("Missing required property 'match'")
            __props__.__dict__["match"] = match
            __props__.__dict__["omit"] = omit
            if smart_class_parameter_id is None and not opts.urn:
                raise TypeError("Missing required property 'smart_class_parameter_id'")
            __props__.__dict__["smart_class_parameter_id"] = smart_class_parameter_id
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
            __props__.__dict__["__meta_"] = None
        super(OverrideValue, __self__).__init__(
            'foreman:index/overrideValue:OverrideValue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            __meta_: Optional[pulumi.Input[bool]] = None,
            match: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            omit: Optional[pulumi.Input[bool]] = None,
            smart_class_parameter_id: Optional[pulumi.Input[int]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'OverrideValue':
        """
        Get an existing OverrideValue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] __meta_: @SUMMARY Smart class parameter override value.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] match: A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
               `domain` or `os`@EXAMPLE { type = "hostgroup" value = "example_group" }
        :param pulumi.Input[bool] omit: When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
               false
        :param pulumi.Input[int] smart_class_parameter_id: ID of the smart class parameter to override.@EXAMPLE 1
        :param pulumi.Input[str] value: Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OverrideValueState.__new__(_OverrideValueState)

        __props__.__dict__["__meta_"] = __meta_
        __props__.__dict__["match"] = match
        __props__.__dict__["omit"] = omit
        __props__.__dict__["smart_class_parameter_id"] = smart_class_parameter_id
        __props__.__dict__["value"] = value
        return OverrideValue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def __meta_(self) -> pulumi.Output[bool]:
        """
        @SUMMARY Smart class parameter override value.
        """
        return pulumi.get(self, "__meta_")

    @property
    @pulumi.getter
    def match(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map containing the match criteria. Must contain two keys: `type` and `value`.Type can be one of `fqdn`, `hostgroup`,
        `domain` or `os`@EXAMPLE { type = "hostgroup" value = "example_group" }
        """
        return pulumi.get(self, "match")

    @property
    @pulumi.getter
    def omit(self) -> pulumi.Output[Optional[bool]]:
        """
        When set to `true` Foreman will not send this parameter in classification output. Default value is `false`.@EXAMPLE
        false
        """
        return pulumi.get(self, "omit")

    @property
    @pulumi.getter(name="smartClassParameterId")
    def smart_class_parameter_id(self) -> pulumi.Output[int]:
        """
        ID of the smart class parameter to override.@EXAMPLE 1
        """
        return pulumi.get(self, "smart_class_parameter_id")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        Smart parameter override value. Hashes and arrays must be JSON encoded.@EXAMPLE jsonencode({ key = "value" })
        """
        return pulumi.get(self, "value")

