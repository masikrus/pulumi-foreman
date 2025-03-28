// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Httpproxy extends pulumi.CustomResource {
    /**
     * Get an existing Httpproxy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HttpproxyState, opts?: pulumi.CustomResourceOptions): Httpproxy {
        return new Httpproxy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'foreman:index/httpproxy:Httpproxy';

    /**
     * Returns true if the given object is an instance of Httpproxy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Httpproxy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Httpproxy.__pulumiType;
    }

    /**
     * @SUMMARY Defining HTTP Proxies that exist on your network allows you to perform various actions through those proxies.
     */
    public /*out*/ readonly __meta_!: pulumi.Output<boolean>;
    /**
     * The name of the http proxy. @EXAMPLE "proxy.company.com"
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Uniform resource locator of the proxy. @EXAMPLE "https://proxy.company.com:8443"
     */
    public readonly url!: pulumi.Output<string>;

    /**
     * Create a Httpproxy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: HttpproxyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: HttpproxyArgs | HttpproxyState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as HttpproxyState | undefined;
            resourceInputs["__meta_"] = state ? state.__meta_ : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["url"] = state ? state.url : undefined;
        } else {
            const args = argsOrState as HttpproxyArgs | undefined;
            if ((!args || args.url === undefined) && !opts.urn) {
                throw new Error("Missing required property 'url'");
            }
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["url"] = args ? args.url : undefined;
            resourceInputs["__meta_"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Httpproxy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Httpproxy resources.
 */
export interface HttpproxyState {
    /**
     * @SUMMARY Defining HTTP Proxies that exist on your network allows you to perform various actions through those proxies.
     */
    __meta_?: pulumi.Input<boolean>;
    /**
     * The name of the http proxy. @EXAMPLE "proxy.company.com"
     */
    name?: pulumi.Input<string>;
    /**
     * Uniform resource locator of the proxy. @EXAMPLE "https://proxy.company.com:8443"
     */
    url?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Httpproxy resource.
 */
export interface HttpproxyArgs {
    /**
     * The name of the http proxy. @EXAMPLE "proxy.company.com"
     */
    name?: pulumi.Input<string>;
    /**
     * Uniform resource locator of the proxy. @EXAMPLE "https://proxy.company.com:8443"
     */
    url: pulumi.Input<string>;
}
