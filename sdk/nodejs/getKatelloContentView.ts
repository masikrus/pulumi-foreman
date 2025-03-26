// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getKatelloContentView(args: GetKatelloContentViewArgs, opts?: pulumi.InvokeOptions): Promise<GetKatelloContentViewResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("foreman:index/getKatelloContentView:getKatelloContentView", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getKatelloContentView.
 */
export interface GetKatelloContentViewArgs {
    name: string;
}

/**
 * A collection of values returned by getKatelloContentView.
 */
export interface GetKatelloContentViewResult {
    readonly autoPublish: boolean;
    readonly componentIds: number[];
    readonly composite: boolean;
    readonly description: string;
    readonly filtered: boolean;
    readonly filters: outputs.GetKatelloContentViewFilter[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly label: string;
    readonly latestVersionId: number;
    readonly name: string;
    readonly organizationId: number;
    readonly repositoryIds: number[];
    readonly solveDependencies: boolean;
}
export function getKatelloContentViewOutput(args: GetKatelloContentViewOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetKatelloContentViewResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("foreman:index/getKatelloContentView:getKatelloContentView", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getKatelloContentView.
 */
export interface GetKatelloContentViewOutputArgs {
    name: pulumi.Input<string>;
}
