// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getKatelloProduct(args: GetKatelloProductArgs, opts?: pulumi.InvokeOptions): Promise<GetKatelloProductResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("foreman:index/getKatelloProduct:getKatelloProduct", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getKatelloProduct.
 */
export interface GetKatelloProductArgs {
    name: string;
}

/**
 * A collection of values returned by getKatelloProduct.
 */
export interface GetKatelloProductResult {
    readonly __meta_: boolean;
    readonly description: string;
    readonly gpgKeyId: number;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly label: string;
    readonly name: string;
    readonly sslCaCertId: number;
    readonly sslClientCertId: number;
    readonly sslClientKeyId: number;
    readonly syncPlanId: number;
}
export function getKatelloProductOutput(args: GetKatelloProductOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetKatelloProductResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("foreman:index/getKatelloProduct:getKatelloProduct", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getKatelloProduct.
 */
export interface GetKatelloProductOutputArgs {
    name: pulumi.Input<string>;
}
