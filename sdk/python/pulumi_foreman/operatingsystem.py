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

__all__ = ['OperatingsystemArgs', 'Operatingsystem']

@pulumi.input_type
class OperatingsystemArgs:
    def __init__(__self__, *,
                 major: pulumi.Input[str],
                 architectures: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 media: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 minor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 partitiontables: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 password_hash: Optional[pulumi.Input[str]] = None,
                 provisioning_templates: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 release_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Operatingsystem resource.
        :param pulumi.Input[str] major: Major release version. @EXAMPLE "7"
        :param pulumi.Input[Sequence[pulumi.Input[int]]] architectures: Identifiers of attached architectures
        :param pulumi.Input[str] description: Additional operating system information.
        :param pulumi.Input[str] family: Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
               `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] media: Identifiers of attached media
        :param pulumi.Input[str] minor: Minor release version. @EXAMPLE "4"
        :param pulumi.Input[str] name: Operating system name. @EXAMPLE "CentOS"
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: A map of parameters that will be saved as operating system parameters in the os config.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] partitiontables: Identifiers of attached partition tables
        :param pulumi.Input[str] password_hash: Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] provisioning_templates: Identifiers of attached provisioning templates
        :param pulumi.Input[str] release_name: Code name or release name for the specific operating system version.
        """
        pulumi.set(__self__, "major", major)
        if architectures is not None:
            pulumi.set(__self__, "architectures", architectures)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if media is not None:
            pulumi.set(__self__, "media", media)
        if minor is not None:
            pulumi.set(__self__, "minor", minor)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if partitiontables is not None:
            pulumi.set(__self__, "partitiontables", partitiontables)
        if password_hash is not None:
            pulumi.set(__self__, "password_hash", password_hash)
        if provisioning_templates is not None:
            pulumi.set(__self__, "provisioning_templates", provisioning_templates)
        if release_name is not None:
            pulumi.set(__self__, "release_name", release_name)

    @property
    @pulumi.getter
    def major(self) -> pulumi.Input[str]:
        """
        Major release version. @EXAMPLE "7"
        """
        return pulumi.get(self, "major")

    @major.setter
    def major(self, value: pulumi.Input[str]):
        pulumi.set(self, "major", value)

    @property
    @pulumi.getter
    def architectures(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Identifiers of attached architectures
        """
        return pulumi.get(self, "architectures")

    @architectures.setter
    def architectures(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "architectures", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Additional operating system information.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[str]]:
        """
        Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
        `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter
    def media(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Identifiers of attached media
        """
        return pulumi.get(self, "media")

    @media.setter
    def media(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "media", value)

    @property
    @pulumi.getter
    def minor(self) -> Optional[pulumi.Input[str]]:
        """
        Minor release version. @EXAMPLE "4"
        """
        return pulumi.get(self, "minor")

    @minor.setter
    def minor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "minor", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Operating system name. @EXAMPLE "CentOS"
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of parameters that will be saved as operating system parameters in the os config.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def partitiontables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Identifiers of attached partition tables
        """
        return pulumi.get(self, "partitiontables")

    @partitiontables.setter
    def partitiontables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "partitiontables", value)

    @property
    @pulumi.getter(name="passwordHash")
    def password_hash(self) -> Optional[pulumi.Input[str]]:
        """
        Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
        """
        return pulumi.get(self, "password_hash")

    @password_hash.setter
    def password_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_hash", value)

    @property
    @pulumi.getter(name="provisioningTemplates")
    def provisioning_templates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Identifiers of attached provisioning templates
        """
        return pulumi.get(self, "provisioning_templates")

    @provisioning_templates.setter
    def provisioning_templates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "provisioning_templates", value)

    @property
    @pulumi.getter(name="releaseName")
    def release_name(self) -> Optional[pulumi.Input[str]]:
        """
        Code name or release name for the specific operating system version.
        """
        return pulumi.get(self, "release_name")

    @release_name.setter
    def release_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "release_name", value)


@pulumi.input_type
class _OperatingsystemState:
    def __init__(__self__, *,
                 __meta_: Optional[pulumi.Input[bool]] = None,
                 architectures: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 major: Optional[pulumi.Input[str]] = None,
                 media: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 minor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 partitiontables: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 password_hash: Optional[pulumi.Input[str]] = None,
                 provisioning_templates: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 release_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Operatingsystem resources.
        :param pulumi.Input[bool] __meta_: @SUMMARY Foreman representation of an operating system.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] architectures: Identifiers of attached architectures
        :param pulumi.Input[str] description: Additional operating system information.
        :param pulumi.Input[str] family: Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
               `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        :param pulumi.Input[str] major: Major release version. @EXAMPLE "7"
        :param pulumi.Input[Sequence[pulumi.Input[int]]] media: Identifiers of attached media
        :param pulumi.Input[str] minor: Minor release version. @EXAMPLE "4"
        :param pulumi.Input[str] name: Operating system name. @EXAMPLE "CentOS"
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: A map of parameters that will be saved as operating system parameters in the os config.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] partitiontables: Identifiers of attached partition tables
        :param pulumi.Input[str] password_hash: Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] provisioning_templates: Identifiers of attached provisioning templates
        :param pulumi.Input[str] release_name: Code name or release name for the specific operating system version.
        :param pulumi.Input[str] title: The operating system's title is a concatentation of the OS name, major, and minor versions to get a full operating
               system release.
        """
        if __meta_ is not None:
            pulumi.set(__self__, "__meta_", __meta_)
        if architectures is not None:
            pulumi.set(__self__, "architectures", architectures)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if major is not None:
            pulumi.set(__self__, "major", major)
        if media is not None:
            pulumi.set(__self__, "media", media)
        if minor is not None:
            pulumi.set(__self__, "minor", minor)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if partitiontables is not None:
            pulumi.set(__self__, "partitiontables", partitiontables)
        if password_hash is not None:
            pulumi.set(__self__, "password_hash", password_hash)
        if provisioning_templates is not None:
            pulumi.set(__self__, "provisioning_templates", provisioning_templates)
        if release_name is not None:
            pulumi.set(__self__, "release_name", release_name)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def __meta_(self) -> Optional[pulumi.Input[bool]]:
        """
        @SUMMARY Foreman representation of an operating system.
        """
        return pulumi.get(self, "__meta_")

    @__meta_.setter
    def __meta_(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "__meta_", value)

    @property
    @pulumi.getter
    def architectures(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Identifiers of attached architectures
        """
        return pulumi.get(self, "architectures")

    @architectures.setter
    def architectures(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "architectures", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Additional operating system information.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[str]]:
        """
        Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
        `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter
    def major(self) -> Optional[pulumi.Input[str]]:
        """
        Major release version. @EXAMPLE "7"
        """
        return pulumi.get(self, "major")

    @major.setter
    def major(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "major", value)

    @property
    @pulumi.getter
    def media(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Identifiers of attached media
        """
        return pulumi.get(self, "media")

    @media.setter
    def media(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "media", value)

    @property
    @pulumi.getter
    def minor(self) -> Optional[pulumi.Input[str]]:
        """
        Minor release version. @EXAMPLE "4"
        """
        return pulumi.get(self, "minor")

    @minor.setter
    def minor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "minor", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Operating system name. @EXAMPLE "CentOS"
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of parameters that will be saved as operating system parameters in the os config.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def partitiontables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Identifiers of attached partition tables
        """
        return pulumi.get(self, "partitiontables")

    @partitiontables.setter
    def partitiontables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "partitiontables", value)

    @property
    @pulumi.getter(name="passwordHash")
    def password_hash(self) -> Optional[pulumi.Input[str]]:
        """
        Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
        """
        return pulumi.get(self, "password_hash")

    @password_hash.setter
    def password_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_hash", value)

    @property
    @pulumi.getter(name="provisioningTemplates")
    def provisioning_templates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Identifiers of attached provisioning templates
        """
        return pulumi.get(self, "provisioning_templates")

    @provisioning_templates.setter
    def provisioning_templates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "provisioning_templates", value)

    @property
    @pulumi.getter(name="releaseName")
    def release_name(self) -> Optional[pulumi.Input[str]]:
        """
        Code name or release name for the specific operating system version.
        """
        return pulumi.get(self, "release_name")

    @release_name.setter
    def release_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "release_name", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The operating system's title is a concatentation of the OS name, major, and minor versions to get a full operating
        system release.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


class Operatingsystem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 architectures: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 major: Optional[pulumi.Input[str]] = None,
                 media: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 minor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 partitiontables: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 password_hash: Optional[pulumi.Input[str]] = None,
                 provisioning_templates: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 release_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Operatingsystem resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] architectures: Identifiers of attached architectures
        :param pulumi.Input[str] description: Additional operating system information.
        :param pulumi.Input[str] family: Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
               `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        :param pulumi.Input[str] major: Major release version. @EXAMPLE "7"
        :param pulumi.Input[Sequence[pulumi.Input[int]]] media: Identifiers of attached media
        :param pulumi.Input[str] minor: Minor release version. @EXAMPLE "4"
        :param pulumi.Input[str] name: Operating system name. @EXAMPLE "CentOS"
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: A map of parameters that will be saved as operating system parameters in the os config.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] partitiontables: Identifiers of attached partition tables
        :param pulumi.Input[str] password_hash: Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] provisioning_templates: Identifiers of attached provisioning templates
        :param pulumi.Input[str] release_name: Code name or release name for the specific operating system version.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OperatingsystemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Operatingsystem resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param OperatingsystemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OperatingsystemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 architectures: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 major: Optional[pulumi.Input[str]] = None,
                 media: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 minor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 partitiontables: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 password_hash: Optional[pulumi.Input[str]] = None,
                 provisioning_templates: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 release_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OperatingsystemArgs.__new__(OperatingsystemArgs)

            __props__.__dict__["architectures"] = architectures
            __props__.__dict__["description"] = description
            __props__.__dict__["family"] = family
            if major is None and not opts.urn:
                raise TypeError("Missing required property 'major'")
            __props__.__dict__["major"] = major
            __props__.__dict__["media"] = media
            __props__.__dict__["minor"] = minor
            __props__.__dict__["name"] = name
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["partitiontables"] = partitiontables
            __props__.__dict__["password_hash"] = password_hash
            __props__.__dict__["provisioning_templates"] = provisioning_templates
            __props__.__dict__["release_name"] = release_name
            __props__.__dict__["__meta_"] = None
            __props__.__dict__["title"] = None
        super(Operatingsystem, __self__).__init__(
            'foreman:index/operatingsystem:Operatingsystem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            __meta_: Optional[pulumi.Input[bool]] = None,
            architectures: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            family: Optional[pulumi.Input[str]] = None,
            major: Optional[pulumi.Input[str]] = None,
            media: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            minor: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            partitiontables: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            password_hash: Optional[pulumi.Input[str]] = None,
            provisioning_templates: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            release_name: Optional[pulumi.Input[str]] = None,
            title: Optional[pulumi.Input[str]] = None) -> 'Operatingsystem':
        """
        Get an existing Operatingsystem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] __meta_: @SUMMARY Foreman representation of an operating system.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] architectures: Identifiers of attached architectures
        :param pulumi.Input[str] description: Additional operating system information.
        :param pulumi.Input[str] family: Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
               `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        :param pulumi.Input[str] major: Major release version. @EXAMPLE "7"
        :param pulumi.Input[Sequence[pulumi.Input[int]]] media: Identifiers of attached media
        :param pulumi.Input[str] minor: Minor release version. @EXAMPLE "4"
        :param pulumi.Input[str] name: Operating system name. @EXAMPLE "CentOS"
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: A map of parameters that will be saved as operating system parameters in the os config.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] partitiontables: Identifiers of attached partition tables
        :param pulumi.Input[str] password_hash: Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] provisioning_templates: Identifiers of attached provisioning templates
        :param pulumi.Input[str] release_name: Code name or release name for the specific operating system version.
        :param pulumi.Input[str] title: The operating system's title is a concatentation of the OS name, major, and minor versions to get a full operating
               system release.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OperatingsystemState.__new__(_OperatingsystemState)

        __props__.__dict__["__meta_"] = __meta_
        __props__.__dict__["architectures"] = architectures
        __props__.__dict__["description"] = description
        __props__.__dict__["family"] = family
        __props__.__dict__["major"] = major
        __props__.__dict__["media"] = media
        __props__.__dict__["minor"] = minor
        __props__.__dict__["name"] = name
        __props__.__dict__["parameters"] = parameters
        __props__.__dict__["partitiontables"] = partitiontables
        __props__.__dict__["password_hash"] = password_hash
        __props__.__dict__["provisioning_templates"] = provisioning_templates
        __props__.__dict__["release_name"] = release_name
        __props__.__dict__["title"] = title
        return Operatingsystem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def __meta_(self) -> pulumi.Output[bool]:
        """
        @SUMMARY Foreman representation of an operating system.
        """
        return pulumi.get(self, "__meta_")

    @property
    @pulumi.getter
    def architectures(self) -> pulumi.Output[Optional[Sequence[int]]]:
        """
        Identifiers of attached architectures
        """
        return pulumi.get(self, "architectures")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Additional operating system information.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def family(self) -> pulumi.Output[Optional[str]]:
        """
        Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
        `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def major(self) -> pulumi.Output[str]:
        """
        Major release version. @EXAMPLE "7"
        """
        return pulumi.get(self, "major")

    @property
    @pulumi.getter
    def media(self) -> pulumi.Output[Optional[Sequence[int]]]:
        """
        Identifiers of attached media
        """
        return pulumi.get(self, "media")

    @property
    @pulumi.getter
    def minor(self) -> pulumi.Output[Optional[str]]:
        """
        Minor release version. @EXAMPLE "4"
        """
        return pulumi.get(self, "minor")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Operating system name. @EXAMPLE "CentOS"
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of parameters that will be saved as operating system parameters in the os config.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def partitiontables(self) -> pulumi.Output[Sequence[int]]:
        """
        Identifiers of attached partition tables
        """
        return pulumi.get(self, "partitiontables")

    @property
    @pulumi.getter(name="passwordHash")
    def password_hash(self) -> pulumi.Output[Optional[str]]:
        """
        Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
        """
        return pulumi.get(self, "password_hash")

    @property
    @pulumi.getter(name="provisioningTemplates")
    def provisioning_templates(self) -> pulumi.Output[Sequence[int]]:
        """
        Identifiers of attached provisioning templates
        """
        return pulumi.get(self, "provisioning_templates")

    @property
    @pulumi.getter(name="releaseName")
    def release_name(self) -> pulumi.Output[Optional[str]]:
        """
        Code name or release name for the specific operating system version.
        """
        return pulumi.get(self, "release_name")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The operating system's title is a concatentation of the OS name, major, and minor versions to get a full operating
        system release.
        """
        return pulumi.get(self, "title")

