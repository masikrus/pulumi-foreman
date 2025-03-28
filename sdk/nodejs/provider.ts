// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The provider type for the foreman package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 */
export class Provider extends pulumi.ProviderResource {
    /** @internal */
    public static readonly __pulumiType = 'foreman';

    /**
     * Returns true if the given object is an instance of Provider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === "pulumi:providers:" + Provider.__pulumiType;
    }

    /**
     * The username to authenticate against Foreman. This can also be set through the environment variable
     * `FOREMAN_CLIENT_PASSWORD`. Defaults to `""`.
     */
    public readonly clientPassword!: pulumi.Output<string | undefined>;
    /**
     * The username to authenticate against Foreman. This can also be set through the environment variable
     * `FOREMAN_CLIENT_USERNAME`. Defaults to `""`.
     */
    public readonly clientUsername!: pulumi.Output<string | undefined>;
    public readonly providerLogfile!: pulumi.Output<string | undefined>;
    /**
     * The level of verbosity for the provider's log file. This setting determines which types of log messages are written and
     * which are ignored. Possible values (from most verbose to least verbose) include 'DEBUG', 'TRACE', 'INFO', 'WARNING',
     * 'ERROR', and 'NONE'. The provider's logs will be written to the location specified by `providerLogfile`. This can also
     * be set through the environment variable `FOREMAN_PROVIDER_LOGLEVEL`. Defaults to `'INFO'`.
     */
    public readonly providerLoglevel!: pulumi.Output<string | undefined>;
    /**
     * The hostname / IP address of the Foreman REST API server
     */
    public readonly serverHostname!: pulumi.Output<string | undefined>;
    /**
     * The protocol the Foreman REST API server is using for communication. Defaults to `"https"`.
     */
    public readonly serverProtocol!: pulumi.Output<string | undefined>;

    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        {
            resourceInputs["clientAuthNegotiate"] = pulumi.output(args ? args.clientAuthNegotiate : undefined).apply(JSON.stringify);
            resourceInputs["clientPassword"] = (args ? args.clientPassword : undefined) ?? utilities.getEnv("FOREMAN_CLIENT_PASSWORD");
            resourceInputs["clientTlsInsecure"] = pulumi.output(args ? args.clientTlsInsecure : undefined).apply(JSON.stringify);
            resourceInputs["clientUsername"] = (args ? args.clientUsername : undefined) ?? utilities.getEnv("FOREMAN_CLIENT_USERNAME");
            resourceInputs["locationId"] = pulumi.output((args ? args.locationId : undefined) ?? utilities.getEnvNumber("FOREMAN_LOCATION_ID")).apply(JSON.stringify);
            resourceInputs["organizationId"] = pulumi.output((args ? args.organizationId : undefined) ?? utilities.getEnvNumber("FOREMAN_ORGANIZATION_ID")).apply(JSON.stringify);
            resourceInputs["providerLogfile"] = args ? args.providerLogfile : undefined;
            resourceInputs["providerLoglevel"] = args ? args.providerLoglevel : undefined;
            resourceInputs["serverHostname"] = (args ? args.serverHostname : undefined) ?? utilities.getEnv("FOREMAN_SERVER_HOSTNAME");
            resourceInputs["serverProtocol"] = (args ? args.serverProtocol : undefined) ?? utilities.getEnv("FOREMAN_PROTOCOL");
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Provider.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    /**
     * Whether or not the client should try to authenticate through the HTTP negotiate mechanism. Defaults to `false`.
     */
    clientAuthNegotiate?: pulumi.Input<boolean>;
    /**
     * The username to authenticate against Foreman. This can also be set through the environment variable
     * `FOREMAN_CLIENT_PASSWORD`. Defaults to `""`.
     */
    clientPassword?: pulumi.Input<string>;
    /**
     * Whether or not to verify the server's certificate. Defaults to `false`.
     */
    clientTlsInsecure?: pulumi.Input<boolean>;
    /**
     * The username to authenticate against Foreman. This can also be set through the environment variable
     * `FOREMAN_CLIENT_USERNAME`. Defaults to `""`.
     */
    clientUsername?: pulumi.Input<string>;
    /**
     * The location for all resources requested and created by the providerDefaults to "0". Set organizationId and locationId
     * to a value < 0 if you need to disable Locations and Organizations on Foreman older than 1.21
     */
    locationId?: pulumi.Input<number>;
    /**
     * The organization for all resource requested and created by the Provider Defaults to "0". Set organizationId and
     * locationId to a value < 0 if you need to disable Locations and Organizations on Foreman older than 1.21
     */
    organizationId?: pulumi.Input<number>;
    providerLogfile?: pulumi.Input<string>;
    /**
     * The level of verbosity for the provider's log file. This setting determines which types of log messages are written and
     * which are ignored. Possible values (from most verbose to least verbose) include 'DEBUG', 'TRACE', 'INFO', 'WARNING',
     * 'ERROR', and 'NONE'. The provider's logs will be written to the location specified by `providerLogfile`. This can also
     * be set through the environment variable `FOREMAN_PROVIDER_LOGLEVEL`. Defaults to `'INFO'`.
     */
    providerLoglevel?: pulumi.Input<string>;
    /**
     * The hostname / IP address of the Foreman REST API server
     */
    serverHostname?: pulumi.Input<string>;
    /**
     * The protocol the Foreman REST API server is using for communication. Defaults to `"https"`.
     */
    serverProtocol?: pulumi.Input<string>;
}
