// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getModel(args: GetModelArgs, opts?: pulumi.InvokeOptions): Promise<GetModelResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("foreman:index/getModel:getModel", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getModel.
 */
export interface GetModelArgs {
    name: string;
}

/**
 * A collection of values returned by getModel.
 */
export interface GetModelResult {
    readonly __meta_: boolean;
    readonly hardwareModel: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly info: string;
    readonly name: string;
    readonly vendorClass: string;
}
export function getModelOutput(args: GetModelOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetModelResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("foreman:index/getModel:getModel", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getModel.
 */
export interface GetModelOutputArgs {
    name: pulumi.Input<string>;
}
