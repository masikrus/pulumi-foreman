// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getComputeresource(args: GetComputeresourceArgs, opts?: pulumi.InvokeOptions): Promise<GetComputeresourceResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("foreman:index/getComputeresource:getComputeresource", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getComputeresource.
 */
export interface GetComputeresourceArgs {
    name: string;
}

/**
 * A collection of values returned by getComputeresource.
 */
export interface GetComputeresourceResult {
    readonly __meta_: boolean;
    readonly cachingenabled: boolean;
    readonly datacenter: string;
    readonly description: string;
    readonly displaytype: string;
    readonly hypervisor: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
    readonly password: string;
    readonly server: string;
    readonly setconsolepassword: boolean;
    readonly url: string;
    readonly user: string;
}
export function getComputeresourceOutput(args: GetComputeresourceOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetComputeresourceResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("foreman:index/getComputeresource:getComputeresource", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getComputeresource.
 */
export interface GetComputeresourceOutputArgs {
    name: pulumi.Input<string>;
}
