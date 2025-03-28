// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getSubnet(args?: GetSubnetArgs, opts?: pulumi.InvokeOptions): Promise<GetSubnetResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("foreman:index/getSubnet:getSubnet", {
        "name": args.name,
        "network": args.network,
    }, opts);
}

/**
 * A collection of arguments for invoking getSubnet.
 */
export interface GetSubnetArgs {
    name?: string;
    network?: string;
}

/**
 * A collection of values returned by getSubnet.
 */
export interface GetSubnetResult {
    readonly bmcId: number;
    readonly bootMode: string;
    readonly description: string;
    readonly dhcpId: number;
    readonly dnsPrimary: string;
    readonly dnsSecondary: string;
    readonly domainIds: number[];
    readonly from: string;
    readonly gateway: string;
    readonly httpbootId: number;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly ipam: string;
    readonly mask: string;
    readonly mtu: number;
    readonly name?: string;
    readonly network?: string;
    readonly networkAddress: string;
    readonly networkType: string;
    readonly templateId: number;
    readonly tftpId: number;
    readonly to: string;
    readonly vlanid: number;
}
export function getSubnetOutput(args?: GetSubnetOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetSubnetResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("foreman:index/getSubnet:getSubnet", {
        "name": args.name,
        "network": args.network,
    }, opts);
}

/**
 * A collection of arguments for invoking getSubnet.
 */
export interface GetSubnetOutputArgs {
    name?: pulumi.Input<string>;
    network?: pulumi.Input<string>;
}
