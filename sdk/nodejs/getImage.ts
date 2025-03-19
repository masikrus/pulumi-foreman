// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getImage(args: GetImageArgs, opts?: pulumi.InvokeOptions): Promise<GetImageResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("foreman:index/getImage:getImage", {
        "computeResourceId": args.computeResourceId,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getImage.
 */
export interface GetImageArgs {
    computeResourceId: number;
    name: string;
}

/**
 * A collection of values returned by getImage.
 */
export interface GetImageResult {
    readonly __meta_: boolean;
    readonly architectureId: number;
    readonly computeResourceId: number;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
    readonly operatingsystemId: number;
    readonly userData: boolean;
    readonly username: string;
    readonly uuid: string;
}
export function getImageOutput(args: GetImageOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetImageResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("foreman:index/getImage:getImage", {
        "computeResourceId": args.computeResourceId,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getImage.
 */
export interface GetImageOutputArgs {
    computeResourceId: pulumi.Input<number>;
    name: pulumi.Input<string>;
}
