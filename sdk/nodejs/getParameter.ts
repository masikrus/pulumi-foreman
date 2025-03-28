// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getParameter(args: GetParameterArgs, opts?: pulumi.InvokeOptions): Promise<GetParameterResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("foreman:index/getParameter:getParameter", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getParameter.
 */
export interface GetParameterArgs {
    name: string;
}

/**
 * A collection of values returned by getParameter.
 */
export interface GetParameterResult {
    readonly domainId: number;
    readonly hostId: number;
    readonly hostgroupId: number;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
    readonly operatingsystemId: number;
    readonly subnetId: number;
    readonly value: string;
}
export function getParameterOutput(args: GetParameterOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetParameterResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("foreman:index/getParameter:getParameter", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getParameter.
 */
export interface GetParameterOutputArgs {
    name: pulumi.Input<string>;
}
