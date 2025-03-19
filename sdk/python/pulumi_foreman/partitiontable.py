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

__all__ = ['PartitiontableArgs', 'Partitiontable']

@pulumi.input_type
class PartitiontableArgs:
    def __init__(__self__, *,
                 layout: pulumi.Input[str],
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 host_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 hostgroup_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 locked: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operatingsystem_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 os_family: Optional[pulumi.Input[str]] = None,
                 snippet: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Partitiontable resource.
        :param pulumi.Input[str] layout: The script that defines the partition table layout. @EXAMPLE "void"
        :param pulumi.Input[str] audit_comment: Any audit comments to associate with the partition table. The audit comment field is saved with the template auditing to
               document the template changes.
        :param pulumi.Input[str] description: Description of the partition table
        :param pulumi.Input[Sequence[pulumi.Input[int]]] host_ids: IDs of the hosts associated with this partition table.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] hostgroup_ids: IDs of the hostgroups associated with this partition table.
        :param pulumi.Input[bool] locked: Whether or not this partition table is locked for editing.
        :param pulumi.Input[str] name: The name of the partition table. @EXAMPLE "AutoYaST LVM"
        :param pulumi.Input[Sequence[pulumi.Input[int]]] operatingsystem_ids: IDs of the operating system associated with this partition table.
        :param pulumi.Input[str] os_family: Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
               `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        :param pulumi.Input[bool] snippet: Whether or not this partition table is a snippet to be embedded in other partition tables.
        """
        pulumi.set(__self__, "layout", layout)
        if audit_comment is not None:
            pulumi.set(__self__, "audit_comment", audit_comment)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if host_ids is not None:
            pulumi.set(__self__, "host_ids", host_ids)
        if hostgroup_ids is not None:
            pulumi.set(__self__, "hostgroup_ids", hostgroup_ids)
        if locked is not None:
            pulumi.set(__self__, "locked", locked)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if operatingsystem_ids is not None:
            pulumi.set(__self__, "operatingsystem_ids", operatingsystem_ids)
        if os_family is not None:
            pulumi.set(__self__, "os_family", os_family)
        if snippet is not None:
            pulumi.set(__self__, "snippet", snippet)

    @property
    @pulumi.getter
    def layout(self) -> pulumi.Input[str]:
        """
        The script that defines the partition table layout. @EXAMPLE "void"
        """
        return pulumi.get(self, "layout")

    @layout.setter
    def layout(self, value: pulumi.Input[str]):
        pulumi.set(self, "layout", value)

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[pulumi.Input[str]]:
        """
        Any audit comments to associate with the partition table. The audit comment field is saved with the template auditing to
        document the template changes.
        """
        return pulumi.get(self, "audit_comment")

    @audit_comment.setter
    def audit_comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "audit_comment", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the partition table
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="hostIds")
    def host_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        IDs of the hosts associated with this partition table.
        """
        return pulumi.get(self, "host_ids")

    @host_ids.setter
    def host_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "host_ids", value)

    @property
    @pulumi.getter(name="hostgroupIds")
    def hostgroup_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        IDs of the hostgroups associated with this partition table.
        """
        return pulumi.get(self, "hostgroup_ids")

    @hostgroup_ids.setter
    def hostgroup_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "hostgroup_ids", value)

    @property
    @pulumi.getter
    def locked(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not this partition table is locked for editing.
        """
        return pulumi.get(self, "locked")

    @locked.setter
    def locked(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "locked", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the partition table. @EXAMPLE "AutoYaST LVM"
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="operatingsystemIds")
    def operatingsystem_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        IDs of the operating system associated with this partition table.
        """
        return pulumi.get(self, "operatingsystem_ids")

    @operatingsystem_ids.setter
    def operatingsystem_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "operatingsystem_ids", value)

    @property
    @pulumi.getter(name="osFamily")
    def os_family(self) -> Optional[pulumi.Input[str]]:
        """
        Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
        `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        """
        return pulumi.get(self, "os_family")

    @os_family.setter
    def os_family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_family", value)

    @property
    @pulumi.getter
    def snippet(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not this partition table is a snippet to be embedded in other partition tables.
        """
        return pulumi.get(self, "snippet")

    @snippet.setter
    def snippet(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "snippet", value)


@pulumi.input_type
class _PartitiontableState:
    def __init__(__self__, *,
                 __meta_: Optional[pulumi.Input[bool]] = None,
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 host_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 hostgroup_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 layout: Optional[pulumi.Input[str]] = None,
                 locked: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operatingsystem_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 os_family: Optional[pulumi.Input[str]] = None,
                 snippet: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Partitiontable resources.
        :param pulumi.Input[bool] __meta_: @SUMMARY The disk partition layout of the host.
        :param pulumi.Input[str] audit_comment: Any audit comments to associate with the partition table. The audit comment field is saved with the template auditing to
               document the template changes.
        :param pulumi.Input[str] description: Description of the partition table
        :param pulumi.Input[Sequence[pulumi.Input[int]]] host_ids: IDs of the hosts associated with this partition table.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] hostgroup_ids: IDs of the hostgroups associated with this partition table.
        :param pulumi.Input[str] layout: The script that defines the partition table layout. @EXAMPLE "void"
        :param pulumi.Input[bool] locked: Whether or not this partition table is locked for editing.
        :param pulumi.Input[str] name: The name of the partition table. @EXAMPLE "AutoYaST LVM"
        :param pulumi.Input[Sequence[pulumi.Input[int]]] operatingsystem_ids: IDs of the operating system associated with this partition table.
        :param pulumi.Input[str] os_family: Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
               `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        :param pulumi.Input[bool] snippet: Whether or not this partition table is a snippet to be embedded in other partition tables.
        """
        if __meta_ is not None:
            pulumi.set(__self__, "__meta_", __meta_)
        if audit_comment is not None:
            pulumi.set(__self__, "audit_comment", audit_comment)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if host_ids is not None:
            pulumi.set(__self__, "host_ids", host_ids)
        if hostgroup_ids is not None:
            pulumi.set(__self__, "hostgroup_ids", hostgroup_ids)
        if layout is not None:
            pulumi.set(__self__, "layout", layout)
        if locked is not None:
            pulumi.set(__self__, "locked", locked)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if operatingsystem_ids is not None:
            pulumi.set(__self__, "operatingsystem_ids", operatingsystem_ids)
        if os_family is not None:
            pulumi.set(__self__, "os_family", os_family)
        if snippet is not None:
            pulumi.set(__self__, "snippet", snippet)

    @property
    @pulumi.getter
    def __meta_(self) -> Optional[pulumi.Input[bool]]:
        """
        @SUMMARY The disk partition layout of the host.
        """
        return pulumi.get(self, "__meta_")

    @__meta_.setter
    def __meta_(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "__meta_", value)

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[pulumi.Input[str]]:
        """
        Any audit comments to associate with the partition table. The audit comment field is saved with the template auditing to
        document the template changes.
        """
        return pulumi.get(self, "audit_comment")

    @audit_comment.setter
    def audit_comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "audit_comment", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the partition table
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="hostIds")
    def host_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        IDs of the hosts associated with this partition table.
        """
        return pulumi.get(self, "host_ids")

    @host_ids.setter
    def host_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "host_ids", value)

    @property
    @pulumi.getter(name="hostgroupIds")
    def hostgroup_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        IDs of the hostgroups associated with this partition table.
        """
        return pulumi.get(self, "hostgroup_ids")

    @hostgroup_ids.setter
    def hostgroup_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "hostgroup_ids", value)

    @property
    @pulumi.getter
    def layout(self) -> Optional[pulumi.Input[str]]:
        """
        The script that defines the partition table layout. @EXAMPLE "void"
        """
        return pulumi.get(self, "layout")

    @layout.setter
    def layout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "layout", value)

    @property
    @pulumi.getter
    def locked(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not this partition table is locked for editing.
        """
        return pulumi.get(self, "locked")

    @locked.setter
    def locked(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "locked", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the partition table. @EXAMPLE "AutoYaST LVM"
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="operatingsystemIds")
    def operatingsystem_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        IDs of the operating system associated with this partition table.
        """
        return pulumi.get(self, "operatingsystem_ids")

    @operatingsystem_ids.setter
    def operatingsystem_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "operatingsystem_ids", value)

    @property
    @pulumi.getter(name="osFamily")
    def os_family(self) -> Optional[pulumi.Input[str]]:
        """
        Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
        `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        """
        return pulumi.get(self, "os_family")

    @os_family.setter
    def os_family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_family", value)

    @property
    @pulumi.getter
    def snippet(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not this partition table is a snippet to be embedded in other partition tables.
        """
        return pulumi.get(self, "snippet")

    @snippet.setter
    def snippet(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "snippet", value)


class Partitiontable(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 host_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 hostgroup_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 layout: Optional[pulumi.Input[str]] = None,
                 locked: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operatingsystem_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 os_family: Optional[pulumi.Input[str]] = None,
                 snippet: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a Partitiontable resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] audit_comment: Any audit comments to associate with the partition table. The audit comment field is saved with the template auditing to
               document the template changes.
        :param pulumi.Input[str] description: Description of the partition table
        :param pulumi.Input[Sequence[pulumi.Input[int]]] host_ids: IDs of the hosts associated with this partition table.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] hostgroup_ids: IDs of the hostgroups associated with this partition table.
        :param pulumi.Input[str] layout: The script that defines the partition table layout. @EXAMPLE "void"
        :param pulumi.Input[bool] locked: Whether or not this partition table is locked for editing.
        :param pulumi.Input[str] name: The name of the partition table. @EXAMPLE "AutoYaST LVM"
        :param pulumi.Input[Sequence[pulumi.Input[int]]] operatingsystem_ids: IDs of the operating system associated with this partition table.
        :param pulumi.Input[str] os_family: Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
               `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        :param pulumi.Input[bool] snippet: Whether or not this partition table is a snippet to be embedded in other partition tables.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PartitiontableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Partitiontable resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param PartitiontableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PartitiontableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 host_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 hostgroup_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 layout: Optional[pulumi.Input[str]] = None,
                 locked: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operatingsystem_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 os_family: Optional[pulumi.Input[str]] = None,
                 snippet: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PartitiontableArgs.__new__(PartitiontableArgs)

            __props__.__dict__["audit_comment"] = audit_comment
            __props__.__dict__["description"] = description
            __props__.__dict__["host_ids"] = host_ids
            __props__.__dict__["hostgroup_ids"] = hostgroup_ids
            if layout is None and not opts.urn:
                raise TypeError("Missing required property 'layout'")
            __props__.__dict__["layout"] = layout
            __props__.__dict__["locked"] = locked
            __props__.__dict__["name"] = name
            __props__.__dict__["operatingsystem_ids"] = operatingsystem_ids
            __props__.__dict__["os_family"] = os_family
            __props__.__dict__["snippet"] = snippet
            __props__.__dict__["__meta_"] = None
        super(Partitiontable, __self__).__init__(
            'foreman:index/partitiontable:Partitiontable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            __meta_: Optional[pulumi.Input[bool]] = None,
            audit_comment: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            host_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            hostgroup_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            layout: Optional[pulumi.Input[str]] = None,
            locked: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            operatingsystem_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            os_family: Optional[pulumi.Input[str]] = None,
            snippet: Optional[pulumi.Input[bool]] = None) -> 'Partitiontable':
        """
        Get an existing Partitiontable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] __meta_: @SUMMARY The disk partition layout of the host.
        :param pulumi.Input[str] audit_comment: Any audit comments to associate with the partition table. The audit comment field is saved with the template auditing to
               document the template changes.
        :param pulumi.Input[str] description: Description of the partition table
        :param pulumi.Input[Sequence[pulumi.Input[int]]] host_ids: IDs of the hosts associated with this partition table.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] hostgroup_ids: IDs of the hostgroups associated with this partition table.
        :param pulumi.Input[str] layout: The script that defines the partition table layout. @EXAMPLE "void"
        :param pulumi.Input[bool] locked: Whether or not this partition table is locked for editing.
        :param pulumi.Input[str] name: The name of the partition table. @EXAMPLE "AutoYaST LVM"
        :param pulumi.Input[Sequence[pulumi.Input[int]]] operatingsystem_ids: IDs of the operating system associated with this partition table.
        :param pulumi.Input[str] os_family: Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
               `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        :param pulumi.Input[bool] snippet: Whether or not this partition table is a snippet to be embedded in other partition tables.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PartitiontableState.__new__(_PartitiontableState)

        __props__.__dict__["__meta_"] = __meta_
        __props__.__dict__["audit_comment"] = audit_comment
        __props__.__dict__["description"] = description
        __props__.__dict__["host_ids"] = host_ids
        __props__.__dict__["hostgroup_ids"] = hostgroup_ids
        __props__.__dict__["layout"] = layout
        __props__.__dict__["locked"] = locked
        __props__.__dict__["name"] = name
        __props__.__dict__["operatingsystem_ids"] = operatingsystem_ids
        __props__.__dict__["os_family"] = os_family
        __props__.__dict__["snippet"] = snippet
        return Partitiontable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def __meta_(self) -> pulumi.Output[bool]:
        """
        @SUMMARY The disk partition layout of the host.
        """
        return pulumi.get(self, "__meta_")

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> pulumi.Output[Optional[str]]:
        """
        Any audit comments to associate with the partition table. The audit comment field is saved with the template auditing to
        document the template changes.
        """
        return pulumi.get(self, "audit_comment")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the partition table
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="hostIds")
    def host_ids(self) -> pulumi.Output[Sequence[int]]:
        """
        IDs of the hosts associated with this partition table.
        """
        return pulumi.get(self, "host_ids")

    @property
    @pulumi.getter(name="hostgroupIds")
    def hostgroup_ids(self) -> pulumi.Output[Sequence[int]]:
        """
        IDs of the hostgroups associated with this partition table.
        """
        return pulumi.get(self, "hostgroup_ids")

    @property
    @pulumi.getter
    def layout(self) -> pulumi.Output[str]:
        """
        The script that defines the partition table layout. @EXAMPLE "void"
        """
        return pulumi.get(self, "layout")

    @property
    @pulumi.getter
    def locked(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not this partition table is locked for editing.
        """
        return pulumi.get(self, "locked")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the partition table. @EXAMPLE "AutoYaST LVM"
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operatingsystemIds")
    def operatingsystem_ids(self) -> pulumi.Output[Sequence[int]]:
        """
        IDs of the operating system associated with this partition table.
        """
        return pulumi.get(self, "operatingsystem_ids")

    @property
    @pulumi.getter(name="osFamily")
    def os_family(self) -> pulumi.Output[Optional[str]]:
        """
        Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
        `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
        """
        return pulumi.get(self, "os_family")

    @property
    @pulumi.getter
    def snippet(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not this partition table is a snippet to be embedded in other partition tables.
        """
        return pulumi.get(self, "snippet")

