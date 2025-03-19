// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as enums from "./types/enums";
import * as utilities from "./utilities";

export class KatelloContentView extends pulumi.CustomResource {
    /**
     * Get an existing KatelloContentView resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KatelloContentViewState, opts?: pulumi.CustomResourceOptions): KatelloContentView {
        return new KatelloContentView(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/katelloContentView:KatelloContentView';

    /**
     * Returns true if the given object is an instance of KatelloContentView.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is KatelloContentView {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === KatelloContentView.__pulumiType;
    }

    /**
     * @SUMMARY (Composite) Content Views create an abstract view on a collection of repositories and allow versioning of these
     * views. Additional fine tuning can be done with package filters.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    /**
     * Relevant for Composite Content Views: 'Automatically publish a new version of the composite content view whenever one of
     * its content views is published. Autopublish will only happen for component views that use the 'Always use latest
     * version' option.'
     */
    public readonly autoPublish!: pulumi.Output<boolean | undefined>;
    /**
     * Relevant for CCVs: list of CV version IDs. @EXAMPLE [1, 4]
     */
    public readonly componentIds!: pulumi.Output<number[] | undefined>;
    /**
     * Is this Content View a Composite CV? @EXAMPLE false
     */
    public readonly composite!: pulumi.Output<boolean | undefined>;
    /**
     * Description for the (composite) content view
     */
    public readonly description!: pulumi.Output<string | undefined>;
    public /*out*/ readonly filtered!: pulumi.Output<boolean>;
    /**
     * Content view filters and their rules.
     */
    public readonly filters!: pulumi.Output<outputs.KatelloContentViewFilter[] | undefined>;
    /**
     * Label for the (composite) content view. Cannot be changed after creation. By default set to the name, with underscores
     * as spaces replacement. @EXAMPLE
     */
    public readonly label!: pulumi.Output<string>;
    /**
     * Holds the ID of the latest published version of a Content View to be used as reference in CCVs
     */
    public /*out*/ readonly latestVersionId!: pulumi.Output<number>;
    /**
     * Name of the (composite) content view. @EXAMPLE "My new CV"
     */
    public readonly name!: pulumi.Output<string>;
    public readonly organizationId!: pulumi.Output<number>;
    /**
     * List of repository IDs. @EXAMPLE [1, 4, 5]
     */
    public readonly repositoryIds!: pulumi.Output<number[]>;
    /**
     * Relevant for Content Views: 'This will solve RPM and module stream dependencies on every publish of this content view.
     * Dependency solving significantly increases publish time (publishes can take over three times as long) and filters will
     * be ignored when adding packages to solve dependencies. Also, certain scenarios involving errata may still cause
     * dependency errors.'
     */
    public readonly solveDependencies!: pulumi.Output<boolean | undefined>;

    /**
     * Create a KatelloContentView resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: KatelloContentViewArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: KatelloContentViewArgs | KatelloContentViewState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as KatelloContentViewState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["autoPublish"] = state ? state.autoPublish : undefined;
            resourceInputs["componentIds"] = state ? state.componentIds : undefined;
            resourceInputs["composite"] = state ? state.composite : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["filtered"] = state ? state.filtered : undefined;
            resourceInputs["filters"] = state ? state.filters : undefined;
            resourceInputs["label"] = state ? state.label : undefined;
            resourceInputs["latestVersionId"] = state ? state.latestVersionId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["organizationId"] = state ? state.organizationId : undefined;
            resourceInputs["repositoryIds"] = state ? state.repositoryIds : undefined;
            resourceInputs["solveDependencies"] = state ? state.solveDependencies : undefined;
        } else {
            const args = argsOrState as KatelloContentViewArgs | undefined;
            resourceInputs["autoPublish"] = args ? args.autoPublish : undefined;
            resourceInputs["componentIds"] = args ? args.componentIds : undefined;
            resourceInputs["composite"] = args ? args.composite : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["filters"] = args ? args.filters : undefined;
            resourceInputs["label"] = args ? args.label : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["organizationId"] = args ? args.organizationId : undefined;
            resourceInputs["repositoryIds"] = args ? args.repositoryIds : undefined;
            resourceInputs["solveDependencies"] = args ? args.solveDependencies : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
            resourceInputs["filtered"] = undefined /*out*/;
            resourceInputs["latestVersionId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(KatelloContentView.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering KatelloContentView resources.
 */
export interface KatelloContentViewState {
    /**
     * @SUMMARY (Composite) Content Views create an abstract view on a collection of repositories and allow versioning of these
     * views. Additional fine tuning can be done with package filters.
     */
    __meta_?: pulumi.Input<boolean>;
    /**
     * Relevant for Composite Content Views: 'Automatically publish a new version of the composite content view whenever one of
     * its content views is published. Autopublish will only happen for component views that use the 'Always use latest
     * version' option.'
     */
    autoPublish?: pulumi.Input<boolean>;
    /**
     * Relevant for CCVs: list of CV version IDs. @EXAMPLE [1, 4]
     */
    componentIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Is this Content View a Composite CV? @EXAMPLE false
     */
    composite?: pulumi.Input<boolean>;
    /**
     * Description for the (composite) content view
     */
    description?: pulumi.Input<string>;
    filtered?: pulumi.Input<boolean>;
    /**
     * Content view filters and their rules.
     */
    filters?: pulumi.Input<pulumi.Input<inputs.KatelloContentViewFilter>[]>;
    /**
     * Label for the (composite) content view. Cannot be changed after creation. By default set to the name, with underscores
     * as spaces replacement. @EXAMPLE
     */
    label?: pulumi.Input<string>;
    /**
     * Holds the ID of the latest published version of a Content View to be used as reference in CCVs
     */
    latestVersionId?: pulumi.Input<number>;
    /**
     * Name of the (composite) content view. @EXAMPLE "My new CV"
     */
    name?: pulumi.Input<string>;
    organizationId?: pulumi.Input<number>;
    /**
     * List of repository IDs. @EXAMPLE [1, 4, 5]
     */
    repositoryIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Relevant for Content Views: 'This will solve RPM and module stream dependencies on every publish of this content view.
     * Dependency solving significantly increases publish time (publishes can take over three times as long) and filters will
     * be ignored when adding packages to solve dependencies. Also, certain scenarios involving errata may still cause
     * dependency errors.'
     */
    solveDependencies?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a KatelloContentView resource.
 */
export interface KatelloContentViewArgs {
    /**
     * Relevant for Composite Content Views: 'Automatically publish a new version of the composite content view whenever one of
     * its content views is published. Autopublish will only happen for component views that use the 'Always use latest
     * version' option.'
     */
    autoPublish?: pulumi.Input<boolean>;
    /**
     * Relevant for CCVs: list of CV version IDs. @EXAMPLE [1, 4]
     */
    componentIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Is this Content View a Composite CV? @EXAMPLE false
     */
    composite?: pulumi.Input<boolean>;
    /**
     * Description for the (composite) content view
     */
    description?: pulumi.Input<string>;
    /**
     * Content view filters and their rules.
     */
    filters?: pulumi.Input<pulumi.Input<inputs.KatelloContentViewFilter>[]>;
    /**
     * Label for the (composite) content view. Cannot be changed after creation. By default set to the name, with underscores
     * as spaces replacement. @EXAMPLE
     */
    label?: pulumi.Input<string>;
    /**
     * Name of the (composite) content view. @EXAMPLE "My new CV"
     */
    name?: pulumi.Input<string>;
    organizationId?: pulumi.Input<number>;
    /**
     * List of repository IDs. @EXAMPLE [1, 4, 5]
     */
    repositoryIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Relevant for Content Views: 'This will solve RPM and module stream dependencies on every publish of this content view.
     * Dependency solving significantly increases publish time (publishes can take over three times as long) and filters will
     * be ignored when adding packages to solve dependencies. Also, certain scenarios involving errata may still cause
     * dependency errors.'
     */
    solveDependencies?: pulumi.Input<boolean>;
}
