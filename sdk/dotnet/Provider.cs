// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    /// <summary>
    /// The provider type for the foreman package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [ForemanResourceType("pulumi:providers:foreman")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// The username to authenticate against Foreman. This can also be set through the environment variable
        /// `FOREMAN_CLIENT_PASSWORD`. Defaults to `""`.
        /// </summary>
        [Output("clientPassword")]
        public Output<string?> ClientPassword { get; private set; } = null!;

        /// <summary>
        /// The username to authenticate against Foreman. This can also be set through the environment variable
        /// `FOREMAN_CLIENT_USERNAME`. Defaults to `""`.
        /// </summary>
        [Output("clientUsername")]
        public Output<string?> ClientUsername { get; private set; } = null!;

        [Output("providerLogfile")]
        public Output<string?> ProviderLogfile { get; private set; } = null!;

        /// <summary>
        /// The level of verbosity for the provider's log file. This setting determines which types of log messages are written and
        /// which are ignored. Possible values (from most verbose to least verbose) include 'DEBUG', 'TRACE', 'INFO', 'WARNING',
        /// 'ERROR', and 'NONE'. The provider's logs will be written to the location specified by `provider_logfile`. This can also
        /// be set through the environment variable `FOREMAN_PROVIDER_LOGLEVEL`. Defaults to `'INFO'`.
        /// </summary>
        [Output("providerLoglevel")]
        public Output<string?> ProviderLoglevel { get; private set; } = null!;

        /// <summary>
        /// The hostname / IP address of the Foreman REST API server
        /// </summary>
        [Output("serverHostname")]
        public Output<string?> ServerHostname { get; private set; } = null!;

        /// <summary>
        /// The protocol the Foreman REST API server is using for communication. Defaults to `"https"`.
        /// </summary>
        [Output("serverProtocol")]
        public Output<string?> ServerProtocol { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("foreman", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether or not the client should try to authenticate through the HTTP negotiate mechanism. Defaults to `false`.
        /// </summary>
        [Input("clientAuthNegotiate", json: true)]
        public Input<bool>? ClientAuthNegotiate { get; set; }

        /// <summary>
        /// The username to authenticate against Foreman. This can also be set through the environment variable
        /// `FOREMAN_CLIENT_PASSWORD`. Defaults to `""`.
        /// </summary>
        [Input("clientPassword")]
        public Input<string>? ClientPassword { get; set; }

        /// <summary>
        /// Whether or not to verify the server's certificate. Defaults to `false`.
        /// </summary>
        [Input("clientTlsInsecure", json: true)]
        public Input<bool>? ClientTlsInsecure { get; set; }

        /// <summary>
        /// The username to authenticate against Foreman. This can also be set through the environment variable
        /// `FOREMAN_CLIENT_USERNAME`. Defaults to `""`.
        /// </summary>
        [Input("clientUsername")]
        public Input<string>? ClientUsername { get; set; }

        /// <summary>
        /// The location for all resources requested and created by the providerDefaults to "0". Set organization_id and location_id
        /// to a value &lt; 0 if you need to disable Locations and Organizations on Foreman older than 1.21
        /// </summary>
        [Input("locationId", json: true)]
        public Input<int>? LocationId { get; set; }

        /// <summary>
        /// The organization for all resource requested and created by the Provider Defaults to "0". Set organization_id and
        /// location_id to a value &lt; 0 if you need to disable Locations and Organizations on Foreman older than 1.21
        /// </summary>
        [Input("organizationId", json: true)]
        public Input<int>? OrganizationId { get; set; }

        [Input("providerLogfile")]
        public Input<string>? ProviderLogfile { get; set; }

        /// <summary>
        /// The level of verbosity for the provider's log file. This setting determines which types of log messages are written and
        /// which are ignored. Possible values (from most verbose to least verbose) include 'DEBUG', 'TRACE', 'INFO', 'WARNING',
        /// 'ERROR', and 'NONE'. The provider's logs will be written to the location specified by `provider_logfile`. This can also
        /// be set through the environment variable `FOREMAN_PROVIDER_LOGLEVEL`. Defaults to `'INFO'`.
        /// </summary>
        [Input("providerLoglevel")]
        public Input<string>? ProviderLoglevel { get; set; }

        /// <summary>
        /// The hostname / IP address of the Foreman REST API server
        /// </summary>
        [Input("serverHostname")]
        public Input<string>? ServerHostname { get; set; }

        /// <summary>
        /// The protocol the Foreman REST API server is using for communication. Defaults to `"https"`.
        /// </summary>
        [Input("serverProtocol")]
        public Input<string>? ServerProtocol { get; set; }

        public ProviderArgs()
        {
            ClientPassword = Utilities.GetEnv("FOREMAN_CLIENT_PASSWORD");
            ClientUsername = Utilities.GetEnv("FOREMAN_CLIENT_USERNAME");
            LocationId = Utilities.GetEnvInt32("FOREMAN_LOCATION_ID");
            OrganizationId = Utilities.GetEnvInt32("FOREMAN_ORGANIZATION_ID");
            ServerHostname = Utilities.GetEnv("FOREMAN_SERVER_HOSTNAME");
            ServerProtocol = Utilities.GetEnv("FOREMAN_PROTOCOL");
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
