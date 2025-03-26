// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getSetting(args: GetSettingArgs, opts?: pulumi.InvokeOptions): Promise<GetSettingResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("foreman:index/getSetting:getSetting", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getSetting.
 */
export interface GetSettingArgs {
    name: string;
}

/**
 * A collection of values returned by getSetting.
 */
export interface GetSettingResult {
    readonly categoryName: string;
    readonly default: string;
    readonly description: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
    readonly readonly: boolean;
    readonly settingsType: string;
    readonly value: string;
}
export function getSettingOutput(args: GetSettingOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetSettingResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("foreman:index/getSetting:getSetting", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getSetting.
 */
export interface GetSettingOutputArgs {
    name: pulumi.Input<string>;
}
