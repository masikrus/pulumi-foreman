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

__all__ = ['KatelloProductArgs', 'KatelloProduct']

@pulumi.input_type
class KatelloProductArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 gpg_key_id: Optional[pulumi.Input[int]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ssl_ca_cert_id: Optional[pulumi.Input[int]] = None,
                 ssl_client_cert_id: Optional[pulumi.Input[int]] = None,
                 ssl_client_key_id: Optional[pulumi.Input[int]] = None,
                 sync_plan_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a KatelloProduct resource.
        :param pulumi.Input[str] description: Product description.@EXAMPLE "A product description"
        :param pulumi.Input[int] gpg_key_id: Identifier of the GPG key.@EXAMPLE
        :param pulumi.Input[str] label: Label for the product. Cannot be changed after creation. By default set to the name, with underscores as spaces
               replacement. @EXAMPLE
        :param pulumi.Input[str] name: Product name.@EXAMPLE "Debian 10"
        :param pulumi.Input[int] ssl_ca_cert_id: Idenifier of the SSL CA Cert.@EXAMPLE
        :param pulumi.Input[int] ssl_client_cert_id: Identifier of the SSL Client Cert.@EXAMPLE
        :param pulumi.Input[int] ssl_client_key_id: Identifier of the SSL Client Key.@EXAMPLE
        :param pulumi.Input[int] sync_plan_id: Plan numeric identifier.@EXAMPLE
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if gpg_key_id is not None:
            pulumi.set(__self__, "gpg_key_id", gpg_key_id)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ssl_ca_cert_id is not None:
            pulumi.set(__self__, "ssl_ca_cert_id", ssl_ca_cert_id)
        if ssl_client_cert_id is not None:
            pulumi.set(__self__, "ssl_client_cert_id", ssl_client_cert_id)
        if ssl_client_key_id is not None:
            pulumi.set(__self__, "ssl_client_key_id", ssl_client_key_id)
        if sync_plan_id is not None:
            pulumi.set(__self__, "sync_plan_id", sync_plan_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Product description.@EXAMPLE "A product description"
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="gpgKeyId")
    def gpg_key_id(self) -> Optional[pulumi.Input[int]]:
        """
        Identifier of the GPG key.@EXAMPLE
        """
        return pulumi.get(self, "gpg_key_id")

    @gpg_key_id.setter
    def gpg_key_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "gpg_key_id", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        Label for the product. Cannot be changed after creation. By default set to the name, with underscores as spaces
        replacement. @EXAMPLE
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Product name.@EXAMPLE "Debian 10"
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sslCaCertId")
    def ssl_ca_cert_id(self) -> Optional[pulumi.Input[int]]:
        """
        Idenifier of the SSL CA Cert.@EXAMPLE
        """
        return pulumi.get(self, "ssl_ca_cert_id")

    @ssl_ca_cert_id.setter
    def ssl_ca_cert_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ssl_ca_cert_id", value)

    @property
    @pulumi.getter(name="sslClientCertId")
    def ssl_client_cert_id(self) -> Optional[pulumi.Input[int]]:
        """
        Identifier of the SSL Client Cert.@EXAMPLE
        """
        return pulumi.get(self, "ssl_client_cert_id")

    @ssl_client_cert_id.setter
    def ssl_client_cert_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ssl_client_cert_id", value)

    @property
    @pulumi.getter(name="sslClientKeyId")
    def ssl_client_key_id(self) -> Optional[pulumi.Input[int]]:
        """
        Identifier of the SSL Client Key.@EXAMPLE
        """
        return pulumi.get(self, "ssl_client_key_id")

    @ssl_client_key_id.setter
    def ssl_client_key_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ssl_client_key_id", value)

    @property
    @pulumi.getter(name="syncPlanId")
    def sync_plan_id(self) -> Optional[pulumi.Input[int]]:
        """
        Plan numeric identifier.@EXAMPLE
        """
        return pulumi.get(self, "sync_plan_id")

    @sync_plan_id.setter
    def sync_plan_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sync_plan_id", value)


@pulumi.input_type
class _KatelloProductState:
    def __init__(__self__, *,
                 __meta_: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gpg_key_id: Optional[pulumi.Input[int]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ssl_ca_cert_id: Optional[pulumi.Input[int]] = None,
                 ssl_client_cert_id: Optional[pulumi.Input[int]] = None,
                 ssl_client_key_id: Optional[pulumi.Input[int]] = None,
                 sync_plan_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering KatelloProduct resources.
        :param pulumi.Input[bool] __meta_: @SUMMARY Poducts are mostly operating systems to which repositories are assigned.
        :param pulumi.Input[str] description: Product description.@EXAMPLE "A product description"
        :param pulumi.Input[int] gpg_key_id: Identifier of the GPG key.@EXAMPLE
        :param pulumi.Input[str] label: Label for the product. Cannot be changed after creation. By default set to the name, with underscores as spaces
               replacement. @EXAMPLE
        :param pulumi.Input[str] name: Product name.@EXAMPLE "Debian 10"
        :param pulumi.Input[int] ssl_ca_cert_id: Idenifier of the SSL CA Cert.@EXAMPLE
        :param pulumi.Input[int] ssl_client_cert_id: Identifier of the SSL Client Cert.@EXAMPLE
        :param pulumi.Input[int] ssl_client_key_id: Identifier of the SSL Client Key.@EXAMPLE
        :param pulumi.Input[int] sync_plan_id: Plan numeric identifier.@EXAMPLE
        """
        if __meta_ is not None:
            pulumi.set(__self__, "__meta_", __meta_)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if gpg_key_id is not None:
            pulumi.set(__self__, "gpg_key_id", gpg_key_id)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ssl_ca_cert_id is not None:
            pulumi.set(__self__, "ssl_ca_cert_id", ssl_ca_cert_id)
        if ssl_client_cert_id is not None:
            pulumi.set(__self__, "ssl_client_cert_id", ssl_client_cert_id)
        if ssl_client_key_id is not None:
            pulumi.set(__self__, "ssl_client_key_id", ssl_client_key_id)
        if sync_plan_id is not None:
            pulumi.set(__self__, "sync_plan_id", sync_plan_id)

    @property
    @pulumi.getter
    def __meta_(self) -> Optional[pulumi.Input[bool]]:
        """
        @SUMMARY Poducts are mostly operating systems to which repositories are assigned.
        """
        return pulumi.get(self, "__meta_")

    @__meta_.setter
    def __meta_(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "__meta_", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Product description.@EXAMPLE "A product description"
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="gpgKeyId")
    def gpg_key_id(self) -> Optional[pulumi.Input[int]]:
        """
        Identifier of the GPG key.@EXAMPLE
        """
        return pulumi.get(self, "gpg_key_id")

    @gpg_key_id.setter
    def gpg_key_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "gpg_key_id", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        Label for the product. Cannot be changed after creation. By default set to the name, with underscores as spaces
        replacement. @EXAMPLE
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Product name.@EXAMPLE "Debian 10"
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sslCaCertId")
    def ssl_ca_cert_id(self) -> Optional[pulumi.Input[int]]:
        """
        Idenifier of the SSL CA Cert.@EXAMPLE
        """
        return pulumi.get(self, "ssl_ca_cert_id")

    @ssl_ca_cert_id.setter
    def ssl_ca_cert_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ssl_ca_cert_id", value)

    @property
    @pulumi.getter(name="sslClientCertId")
    def ssl_client_cert_id(self) -> Optional[pulumi.Input[int]]:
        """
        Identifier of the SSL Client Cert.@EXAMPLE
        """
        return pulumi.get(self, "ssl_client_cert_id")

    @ssl_client_cert_id.setter
    def ssl_client_cert_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ssl_client_cert_id", value)

    @property
    @pulumi.getter(name="sslClientKeyId")
    def ssl_client_key_id(self) -> Optional[pulumi.Input[int]]:
        """
        Identifier of the SSL Client Key.@EXAMPLE
        """
        return pulumi.get(self, "ssl_client_key_id")

    @ssl_client_key_id.setter
    def ssl_client_key_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ssl_client_key_id", value)

    @property
    @pulumi.getter(name="syncPlanId")
    def sync_plan_id(self) -> Optional[pulumi.Input[int]]:
        """
        Plan numeric identifier.@EXAMPLE
        """
        return pulumi.get(self, "sync_plan_id")

    @sync_plan_id.setter
    def sync_plan_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sync_plan_id", value)


class KatelloProduct(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gpg_key_id: Optional[pulumi.Input[int]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ssl_ca_cert_id: Optional[pulumi.Input[int]] = None,
                 ssl_client_cert_id: Optional[pulumi.Input[int]] = None,
                 ssl_client_key_id: Optional[pulumi.Input[int]] = None,
                 sync_plan_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a KatelloProduct resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Product description.@EXAMPLE "A product description"
        :param pulumi.Input[int] gpg_key_id: Identifier of the GPG key.@EXAMPLE
        :param pulumi.Input[str] label: Label for the product. Cannot be changed after creation. By default set to the name, with underscores as spaces
               replacement. @EXAMPLE
        :param pulumi.Input[str] name: Product name.@EXAMPLE "Debian 10"
        :param pulumi.Input[int] ssl_ca_cert_id: Idenifier of the SSL CA Cert.@EXAMPLE
        :param pulumi.Input[int] ssl_client_cert_id: Identifier of the SSL Client Cert.@EXAMPLE
        :param pulumi.Input[int] ssl_client_key_id: Identifier of the SSL Client Key.@EXAMPLE
        :param pulumi.Input[int] sync_plan_id: Plan numeric identifier.@EXAMPLE
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[KatelloProductArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a KatelloProduct resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param KatelloProductArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KatelloProductArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gpg_key_id: Optional[pulumi.Input[int]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ssl_ca_cert_id: Optional[pulumi.Input[int]] = None,
                 ssl_client_cert_id: Optional[pulumi.Input[int]] = None,
                 ssl_client_key_id: Optional[pulumi.Input[int]] = None,
                 sync_plan_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KatelloProductArgs.__new__(KatelloProductArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["gpg_key_id"] = gpg_key_id
            __props__.__dict__["label"] = label
            __props__.__dict__["name"] = name
            __props__.__dict__["ssl_ca_cert_id"] = ssl_ca_cert_id
            __props__.__dict__["ssl_client_cert_id"] = ssl_client_cert_id
            __props__.__dict__["ssl_client_key_id"] = ssl_client_key_id
            __props__.__dict__["sync_plan_id"] = sync_plan_id
            __props__.__dict__["__meta_"] = None
        super(KatelloProduct, __self__).__init__(
            'foreman:index/katelloProduct:KatelloProduct',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            __meta_: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            gpg_key_id: Optional[pulumi.Input[int]] = None,
            label: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            ssl_ca_cert_id: Optional[pulumi.Input[int]] = None,
            ssl_client_cert_id: Optional[pulumi.Input[int]] = None,
            ssl_client_key_id: Optional[pulumi.Input[int]] = None,
            sync_plan_id: Optional[pulumi.Input[int]] = None) -> 'KatelloProduct':
        """
        Get an existing KatelloProduct resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] __meta_: @SUMMARY Poducts are mostly operating systems to which repositories are assigned.
        :param pulumi.Input[str] description: Product description.@EXAMPLE "A product description"
        :param pulumi.Input[int] gpg_key_id: Identifier of the GPG key.@EXAMPLE
        :param pulumi.Input[str] label: Label for the product. Cannot be changed after creation. By default set to the name, with underscores as spaces
               replacement. @EXAMPLE
        :param pulumi.Input[str] name: Product name.@EXAMPLE "Debian 10"
        :param pulumi.Input[int] ssl_ca_cert_id: Idenifier of the SSL CA Cert.@EXAMPLE
        :param pulumi.Input[int] ssl_client_cert_id: Identifier of the SSL Client Cert.@EXAMPLE
        :param pulumi.Input[int] ssl_client_key_id: Identifier of the SSL Client Key.@EXAMPLE
        :param pulumi.Input[int] sync_plan_id: Plan numeric identifier.@EXAMPLE
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KatelloProductState.__new__(_KatelloProductState)

        __props__.__dict__["__meta_"] = __meta_
        __props__.__dict__["description"] = description
        __props__.__dict__["gpg_key_id"] = gpg_key_id
        __props__.__dict__["label"] = label
        __props__.__dict__["name"] = name
        __props__.__dict__["ssl_ca_cert_id"] = ssl_ca_cert_id
        __props__.__dict__["ssl_client_cert_id"] = ssl_client_cert_id
        __props__.__dict__["ssl_client_key_id"] = ssl_client_key_id
        __props__.__dict__["sync_plan_id"] = sync_plan_id
        return KatelloProduct(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def __meta_(self) -> pulumi.Output[bool]:
        """
        @SUMMARY Poducts are mostly operating systems to which repositories are assigned.
        """
        return pulumi.get(self, "__meta_")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Product description.@EXAMPLE "A product description"
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="gpgKeyId")
    def gpg_key_id(self) -> pulumi.Output[Optional[int]]:
        """
        Identifier of the GPG key.@EXAMPLE
        """
        return pulumi.get(self, "gpg_key_id")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        """
        Label for the product. Cannot be changed after creation. By default set to the name, with underscores as spaces
        replacement. @EXAMPLE
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Product name.@EXAMPLE "Debian 10"
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sslCaCertId")
    def ssl_ca_cert_id(self) -> pulumi.Output[Optional[int]]:
        """
        Idenifier of the SSL CA Cert.@EXAMPLE
        """
        return pulumi.get(self, "ssl_ca_cert_id")

    @property
    @pulumi.getter(name="sslClientCertId")
    def ssl_client_cert_id(self) -> pulumi.Output[Optional[int]]:
        """
        Identifier of the SSL Client Cert.@EXAMPLE
        """
        return pulumi.get(self, "ssl_client_cert_id")

    @property
    @pulumi.getter(name="sslClientKeyId")
    def ssl_client_key_id(self) -> pulumi.Output[Optional[int]]:
        """
        Identifier of the SSL Client Key.@EXAMPLE
        """
        return pulumi.get(self, "ssl_client_key_id")

    @property
    @pulumi.getter(name="syncPlanId")
    def sync_plan_id(self) -> pulumi.Output[Optional[int]]:
        """
        Plan numeric identifier.@EXAMPLE
        """
        return pulumi.get(self, "sync_plan_id")

