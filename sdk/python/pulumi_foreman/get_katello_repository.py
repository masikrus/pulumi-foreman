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
    'GetKatelloRepositoryResult',
    'AwaitableGetKatelloRepositoryResult',
    'get_katello_repository',
    'get_katello_repository_output',
]

@pulumi.output_type
class GetKatelloRepositoryResult:
    """
    A collection of values returned by getKatelloRepository.
    """
    def __init__(__self__, __meta_=None, ansible_collection_requirements=None, checksum_type=None, content_type=None, deb_architectures=None, deb_components=None, deb_releases=None, description=None, docker_tags_whitelist=None, docker_upstream_name=None, download_concurrency=None, download_policy=None, gpg_key_id=None, http_proxy_id=None, http_proxy_policy=None, id=None, ignorable_content=None, ignore_global_proxy=None, label=None, mirror_on_sync=None, mirroring_policy=None, name=None, product_id=None, unprotected=None, upstream_password=None, upstream_username=None, url=None, verify_ssl_on_sync=None):
        if __meta_ and not isinstance(__meta_, bool):
            raise TypeError("Expected argument '__meta_' to be a bool")
        pulumi.set(__self__, "__meta_", __meta_)
        if ansible_collection_requirements and not isinstance(ansible_collection_requirements, str):
            raise TypeError("Expected argument 'ansible_collection_requirements' to be a str")
        pulumi.set(__self__, "ansible_collection_requirements", ansible_collection_requirements)
        if checksum_type and not isinstance(checksum_type, str):
            raise TypeError("Expected argument 'checksum_type' to be a str")
        pulumi.set(__self__, "checksum_type", checksum_type)
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if deb_architectures and not isinstance(deb_architectures, str):
            raise TypeError("Expected argument 'deb_architectures' to be a str")
        pulumi.set(__self__, "deb_architectures", deb_architectures)
        if deb_components and not isinstance(deb_components, str):
            raise TypeError("Expected argument 'deb_components' to be a str")
        pulumi.set(__self__, "deb_components", deb_components)
        if deb_releases and not isinstance(deb_releases, str):
            raise TypeError("Expected argument 'deb_releases' to be a str")
        pulumi.set(__self__, "deb_releases", deb_releases)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if docker_tags_whitelist and not isinstance(docker_tags_whitelist, str):
            raise TypeError("Expected argument 'docker_tags_whitelist' to be a str")
        pulumi.set(__self__, "docker_tags_whitelist", docker_tags_whitelist)
        if docker_upstream_name and not isinstance(docker_upstream_name, str):
            raise TypeError("Expected argument 'docker_upstream_name' to be a str")
        pulumi.set(__self__, "docker_upstream_name", docker_upstream_name)
        if download_concurrency and not isinstance(download_concurrency, int):
            raise TypeError("Expected argument 'download_concurrency' to be a int")
        pulumi.set(__self__, "download_concurrency", download_concurrency)
        if download_policy and not isinstance(download_policy, str):
            raise TypeError("Expected argument 'download_policy' to be a str")
        pulumi.set(__self__, "download_policy", download_policy)
        if gpg_key_id and not isinstance(gpg_key_id, int):
            raise TypeError("Expected argument 'gpg_key_id' to be a int")
        pulumi.set(__self__, "gpg_key_id", gpg_key_id)
        if http_proxy_id and not isinstance(http_proxy_id, int):
            raise TypeError("Expected argument 'http_proxy_id' to be a int")
        pulumi.set(__self__, "http_proxy_id", http_proxy_id)
        if http_proxy_policy and not isinstance(http_proxy_policy, str):
            raise TypeError("Expected argument 'http_proxy_policy' to be a str")
        pulumi.set(__self__, "http_proxy_policy", http_proxy_policy)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ignorable_content and not isinstance(ignorable_content, str):
            raise TypeError("Expected argument 'ignorable_content' to be a str")
        pulumi.set(__self__, "ignorable_content", ignorable_content)
        if ignore_global_proxy and not isinstance(ignore_global_proxy, bool):
            raise TypeError("Expected argument 'ignore_global_proxy' to be a bool")
        pulumi.set(__self__, "ignore_global_proxy", ignore_global_proxy)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if mirror_on_sync and not isinstance(mirror_on_sync, bool):
            raise TypeError("Expected argument 'mirror_on_sync' to be a bool")
        pulumi.set(__self__, "mirror_on_sync", mirror_on_sync)
        if mirroring_policy and not isinstance(mirroring_policy, str):
            raise TypeError("Expected argument 'mirroring_policy' to be a str")
        pulumi.set(__self__, "mirroring_policy", mirroring_policy)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if product_id and not isinstance(product_id, int):
            raise TypeError("Expected argument 'product_id' to be a int")
        pulumi.set(__self__, "product_id", product_id)
        if unprotected and not isinstance(unprotected, bool):
            raise TypeError("Expected argument 'unprotected' to be a bool")
        pulumi.set(__self__, "unprotected", unprotected)
        if upstream_password and not isinstance(upstream_password, str):
            raise TypeError("Expected argument 'upstream_password' to be a str")
        pulumi.set(__self__, "upstream_password", upstream_password)
        if upstream_username and not isinstance(upstream_username, str):
            raise TypeError("Expected argument 'upstream_username' to be a str")
        pulumi.set(__self__, "upstream_username", upstream_username)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)
        if verify_ssl_on_sync and not isinstance(verify_ssl_on_sync, bool):
            raise TypeError("Expected argument 'verify_ssl_on_sync' to be a bool")
        pulumi.set(__self__, "verify_ssl_on_sync", verify_ssl_on_sync)

    @property
    @pulumi.getter
    def __meta_(self) -> bool:
        return pulumi.get(self, "__meta_")

    @property
    @pulumi.getter(name="ansibleCollectionRequirements")
    def ansible_collection_requirements(self) -> str:
        return pulumi.get(self, "ansible_collection_requirements")

    @property
    @pulumi.getter(name="checksumType")
    def checksum_type(self) -> str:
        return pulumi.get(self, "checksum_type")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> str:
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="debArchitectures")
    def deb_architectures(self) -> str:
        return pulumi.get(self, "deb_architectures")

    @property
    @pulumi.getter(name="debComponents")
    def deb_components(self) -> str:
        return pulumi.get(self, "deb_components")

    @property
    @pulumi.getter(name="debReleases")
    def deb_releases(self) -> str:
        return pulumi.get(self, "deb_releases")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dockerTagsWhitelist")
    def docker_tags_whitelist(self) -> str:
        return pulumi.get(self, "docker_tags_whitelist")

    @property
    @pulumi.getter(name="dockerUpstreamName")
    def docker_upstream_name(self) -> str:
        return pulumi.get(self, "docker_upstream_name")

    @property
    @pulumi.getter(name="downloadConcurrency")
    def download_concurrency(self) -> int:
        return pulumi.get(self, "download_concurrency")

    @property
    @pulumi.getter(name="downloadPolicy")
    def download_policy(self) -> str:
        return pulumi.get(self, "download_policy")

    @property
    @pulumi.getter(name="gpgKeyId")
    def gpg_key_id(self) -> int:
        return pulumi.get(self, "gpg_key_id")

    @property
    @pulumi.getter(name="httpProxyId")
    def http_proxy_id(self) -> int:
        return pulumi.get(self, "http_proxy_id")

    @property
    @pulumi.getter(name="httpProxyPolicy")
    def http_proxy_policy(self) -> str:
        return pulumi.get(self, "http_proxy_policy")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ignorableContent")
    def ignorable_content(self) -> str:
        return pulumi.get(self, "ignorable_content")

    @property
    @pulumi.getter(name="ignoreGlobalProxy")
    def ignore_global_proxy(self) -> bool:
        return pulumi.get(self, "ignore_global_proxy")

    @property
    @pulumi.getter
    def label(self) -> str:
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="mirrorOnSync")
    def mirror_on_sync(self) -> bool:
        return pulumi.get(self, "mirror_on_sync")

    @property
    @pulumi.getter(name="mirroringPolicy")
    def mirroring_policy(self) -> str:
        return pulumi.get(self, "mirroring_policy")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> int:
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter
    def unprotected(self) -> bool:
        return pulumi.get(self, "unprotected")

    @property
    @pulumi.getter(name="upstreamPassword")
    def upstream_password(self) -> str:
        return pulumi.get(self, "upstream_password")

    @property
    @pulumi.getter(name="upstreamUsername")
    def upstream_username(self) -> str:
        return pulumi.get(self, "upstream_username")

    @property
    @pulumi.getter
    def url(self) -> str:
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="verifySslOnSync")
    def verify_ssl_on_sync(self) -> bool:
        return pulumi.get(self, "verify_ssl_on_sync")


class AwaitableGetKatelloRepositoryResult(GetKatelloRepositoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKatelloRepositoryResult(
            __meta_=self.__meta_,
            ansible_collection_requirements=self.ansible_collection_requirements,
            checksum_type=self.checksum_type,
            content_type=self.content_type,
            deb_architectures=self.deb_architectures,
            deb_components=self.deb_components,
            deb_releases=self.deb_releases,
            description=self.description,
            docker_tags_whitelist=self.docker_tags_whitelist,
            docker_upstream_name=self.docker_upstream_name,
            download_concurrency=self.download_concurrency,
            download_policy=self.download_policy,
            gpg_key_id=self.gpg_key_id,
            http_proxy_id=self.http_proxy_id,
            http_proxy_policy=self.http_proxy_policy,
            id=self.id,
            ignorable_content=self.ignorable_content,
            ignore_global_proxy=self.ignore_global_proxy,
            label=self.label,
            mirror_on_sync=self.mirror_on_sync,
            mirroring_policy=self.mirroring_policy,
            name=self.name,
            product_id=self.product_id,
            unprotected=self.unprotected,
            upstream_password=self.upstream_password,
            upstream_username=self.upstream_username,
            url=self.url,
            verify_ssl_on_sync=self.verify_ssl_on_sync)


def get_katello_repository(name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKatelloRepositoryResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('foreman:index/getKatelloRepository:getKatelloRepository', __args__, opts=opts, typ=GetKatelloRepositoryResult).value

    return AwaitableGetKatelloRepositoryResult(
        __meta_=pulumi.get(__ret__, '__meta_'),
        ansible_collection_requirements=pulumi.get(__ret__, 'ansible_collection_requirements'),
        checksum_type=pulumi.get(__ret__, 'checksum_type'),
        content_type=pulumi.get(__ret__, 'content_type'),
        deb_architectures=pulumi.get(__ret__, 'deb_architectures'),
        deb_components=pulumi.get(__ret__, 'deb_components'),
        deb_releases=pulumi.get(__ret__, 'deb_releases'),
        description=pulumi.get(__ret__, 'description'),
        docker_tags_whitelist=pulumi.get(__ret__, 'docker_tags_whitelist'),
        docker_upstream_name=pulumi.get(__ret__, 'docker_upstream_name'),
        download_concurrency=pulumi.get(__ret__, 'download_concurrency'),
        download_policy=pulumi.get(__ret__, 'download_policy'),
        gpg_key_id=pulumi.get(__ret__, 'gpg_key_id'),
        http_proxy_id=pulumi.get(__ret__, 'http_proxy_id'),
        http_proxy_policy=pulumi.get(__ret__, 'http_proxy_policy'),
        id=pulumi.get(__ret__, 'id'),
        ignorable_content=pulumi.get(__ret__, 'ignorable_content'),
        ignore_global_proxy=pulumi.get(__ret__, 'ignore_global_proxy'),
        label=pulumi.get(__ret__, 'label'),
        mirror_on_sync=pulumi.get(__ret__, 'mirror_on_sync'),
        mirroring_policy=pulumi.get(__ret__, 'mirroring_policy'),
        name=pulumi.get(__ret__, 'name'),
        product_id=pulumi.get(__ret__, 'product_id'),
        unprotected=pulumi.get(__ret__, 'unprotected'),
        upstream_password=pulumi.get(__ret__, 'upstream_password'),
        upstream_username=pulumi.get(__ret__, 'upstream_username'),
        url=pulumi.get(__ret__, 'url'),
        verify_ssl_on_sync=pulumi.get(__ret__, 'verify_ssl_on_sync'))
def get_katello_repository_output(name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetKatelloRepositoryResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('foreman:index/getKatelloRepository:getKatelloRepository', __args__, opts=opts, typ=GetKatelloRepositoryResult)
    return __ret__.apply(lambda __response__: GetKatelloRepositoryResult(
        __meta_=pulumi.get(__response__, '__meta_'),
        ansible_collection_requirements=pulumi.get(__response__, 'ansible_collection_requirements'),
        checksum_type=pulumi.get(__response__, 'checksum_type'),
        content_type=pulumi.get(__response__, 'content_type'),
        deb_architectures=pulumi.get(__response__, 'deb_architectures'),
        deb_components=pulumi.get(__response__, 'deb_components'),
        deb_releases=pulumi.get(__response__, 'deb_releases'),
        description=pulumi.get(__response__, 'description'),
        docker_tags_whitelist=pulumi.get(__response__, 'docker_tags_whitelist'),
        docker_upstream_name=pulumi.get(__response__, 'docker_upstream_name'),
        download_concurrency=pulumi.get(__response__, 'download_concurrency'),
        download_policy=pulumi.get(__response__, 'download_policy'),
        gpg_key_id=pulumi.get(__response__, 'gpg_key_id'),
        http_proxy_id=pulumi.get(__response__, 'http_proxy_id'),
        http_proxy_policy=pulumi.get(__response__, 'http_proxy_policy'),
        id=pulumi.get(__response__, 'id'),
        ignorable_content=pulumi.get(__response__, 'ignorable_content'),
        ignore_global_proxy=pulumi.get(__response__, 'ignore_global_proxy'),
        label=pulumi.get(__response__, 'label'),
        mirror_on_sync=pulumi.get(__response__, 'mirror_on_sync'),
        mirroring_policy=pulumi.get(__response__, 'mirroring_policy'),
        name=pulumi.get(__response__, 'name'),
        product_id=pulumi.get(__response__, 'product_id'),
        unprotected=pulumi.get(__response__, 'unprotected'),
        upstream_password=pulumi.get(__response__, 'upstream_password'),
        upstream_username=pulumi.get(__response__, 'upstream_username'),
        url=pulumi.get(__response__, 'url'),
        verify_ssl_on_sync=pulumi.get(__response__, 'verify_ssl_on_sync')))
