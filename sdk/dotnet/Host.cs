// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    [ForemanResourceType("foreman:index/host:Host")]
    public partial class Host : global::Pulumi.CustomResource
    {
        /// <summary>
        /// @SUMMARY A host managed by Foreman.
        /// </summary>
        [Output("__meta_")]
        public Output<bool> __meta_ { get; private set; } = null!;

        /// <summary>
        /// ID of the architecture of this host
        /// </summary>
        [Output("architectureId")]
        public Output<int> ArchitectureId { get; private set; } = null!;

        [Output("bmcSuccess")]
        public Output<bool?> BmcSuccess { get; private set; } = null!;

        /// <summary>
        /// Add additional information about this host.Note: Changes to this attribute will trigger a host rebuild.
        /// </summary>
        [Output("comment")]
        public Output<string> Comment { get; private set; } = null!;

        /// <summary>
        /// Hypervisor specific VM options. Must be a JSON string, as every compute provider has different attributes schema
        /// </summary>
        [Output("computeAttributes")]
        public Output<string> ComputeAttributes { get; private set; } = null!;

        [Output("computeProfileId")]
        public Output<int> ComputeProfileId { get; private set; } = null!;

        [Output("computeResourceId")]
        public Output<int> ComputeResourceId { get; private set; } = null!;

        /// <summary>
        /// IDs of the applied config groups.
        /// </summary>
        [Output("configGroupIds")]
        public Output<ImmutableArray<int>> ConfigGroupIds { get; private set; } = null!;

        /// <summary>
        /// ID of the domain to assign to the host.
        /// </summary>
        [Output("domainId")]
        public Output<int> DomainId { get; private set; } = null!;

        /// <summary>
        /// The domain name of the host.
        /// </summary>
        [Output("domainName")]
        public Output<string> DomainName { get; private set; } = null!;

        /// <summary>
        /// Enables PMI/BMC functionality. On create and update calls, having this enabled will force a host to poweroff, set next
        /// boot to PXE and power on. Defaults to `false`.
        /// </summary>
        [Output("enableBmc")]
        public Output<bool?> EnableBmc { get; private set; } = null!;

        /// <summary>
        /// ID of the environment to assign to the host.
        /// </summary>
        [Output("environmentId")]
        public Output<int> EnvironmentId { get; private set; } = null!;

        /// <summary>
        /// Host fully qualified domain name. Read-only value to be used in variables. @EXAMPLE "compute01.dc1.company.com"
        /// </summary>
        [Output("fqdn")]
        public Output<string> Fqdn { get; private set; } = null!;

        /// <summary>
        /// ID of the hostgroup to assign to the host.
        /// </summary>
        [Output("hostgroupId")]
        public Output<int> HostgroupId { get; private set; } = null!;

        /// <summary>
        /// ID of an image to be used as base for this host when cloning
        /// </summary>
        [Output("imageId")]
        public Output<int> ImageId { get; private set; } = null!;

        /// <summary>
        /// Host interface information.
        /// </summary>
        [Output("interfacesAttributes")]
        public Output<ImmutableArray<Outputs.HostInterfacesAttribute>> InterfacesAttributes { get; private set; } = null!;

        /// <summary>
        /// Manage power operations, e.g. power on, if host's build flag will be enabled.
        /// </summary>
        [Output("managePowerOperations")]
        public Output<bool?> ManagePowerOperations { get; private set; } = null!;

        /// <summary>
        /// Whether or not this host is managed by Foreman. Create host only, don't set build status or manage power states.
        /// </summary>
        [Output("managed")]
        public Output<bool?> Managed { get; private set; } = null!;

        /// <summary>
        /// ID of the medium mounted on the host.
        /// </summary>
        [Output("mediumId")]
        public Output<int> MediumId { get; private set; } = null!;

        /// <summary>
        /// ID of the hardware model if applicable
        /// </summary>
        [Output("modelId")]
        public Output<int> ModelId { get; private set; } = null!;

        /// <summary>
        /// Name of this host as stored in Foreman. Can be short name or FQDN, depending on your Foreman settings (especially the
        /// setting 'append_domain_name_for_hosts').
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// ID of the operating system to put on the host.
        /// </summary>
        [Output("operatingsystemId")]
        public Output<int> OperatingsystemId { get; private set; } = null!;

        /// <summary>
        /// ID of the user or usergroup that owns the host.
        /// </summary>
        [Output("ownerId")]
        public Output<int> OwnerId { get; private set; } = null!;

        /// <summary>
        /// Owner of the host, must be either User ot Usergroup
        /// </summary>
        [Output("ownerType")]
        public Output<string> OwnerType { get; private set; } = null!;

        /// <summary>
        /// A map of parameters that will be saved as host parameters in the machine config.
        /// </summary>
        [Output("parameters")]
        public Output<ImmutableDictionary<string, string>> Parameters { get; private set; } = null!;

        /// <summary>
        /// Sets the provision method in Foreman for this host: either network-based ('build') or image-based ('image')
        /// </summary>
        [Output("provisionMethod")]
        public Output<string?> ProvisionMethod { get; private set; } = null!;

        /// <summary>
        /// ID of the partition table the host should use
        /// </summary>
        [Output("ptableId")]
        public Output<int> PtableId { get; private set; } = null!;

        /// <summary>
        /// IDs of the applied puppet classes.
        /// </summary>
        [Output("puppetClassIds")]
        public Output<ImmutableArray<int>> PuppetClassIds { get; private set; } = null!;

        /// <summary>
        /// Number of times to retry on a failed attempt to register or delete a host in foreman.
        /// </summary>
        [Output("retryCount")]
        public Output<int?> RetryCount { get; private set; } = null!;

        /// <summary>
        /// Default root password
        /// </summary>
        [Output("rootPassword")]
        public Output<string?> RootPassword { get; private set; } = null!;

        /// <summary>
        /// Sets the Foreman-internal 'build' flag on this host - even if it is already built completely.
        /// </summary>
        [Output("setBuildFlag")]
        public Output<bool?> SetBuildFlag { get; private set; } = null!;

        /// <summary>
        /// The short name of this host. Example: when the FQDN is 'host01.example.org', then 'host01' is the short name.
        /// </summary>
        [Output("shortname")]
        public Output<string> Shortname { get; private set; } = null!;

        /// <summary>
        /// ID of the subnet the host should be placed in
        /// </summary>
        [Output("subnetId")]
        public Output<int> SubnetId { get; private set; } = null!;

        /// <summary>
        /// Build token. Can be used to signal to Foreman that a host build is complete.
        /// </summary>
        [Output("token")]
        public Output<string> Token { get; private set; } = null!;


        /// <summary>
        /// Create a Host resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Host(string name, HostArgs? args = null, CustomResourceOptions? options = null)
            : base("foreman:index/host:Host", name, args ?? new HostArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Host(string name, Input<string> id, HostState? state = null, CustomResourceOptions? options = null)
            : base("foreman:index/host:Host", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                AdditionalSecretOutputs =
                {
                    "rootPassword",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Host resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Host Get(string name, Input<string> id, HostState? state = null, CustomResourceOptions? options = null)
        {
            return new Host(name, id, state, options);
        }
    }

    public sealed class HostArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the architecture of this host
        /// </summary>
        [Input("architectureId")]
        public Input<int>? ArchitectureId { get; set; }

        [Input("bmcSuccess")]
        public Input<bool>? BmcSuccess { get; set; }

        /// <summary>
        /// Add additional information about this host.Note: Changes to this attribute will trigger a host rebuild.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// Hypervisor specific VM options. Must be a JSON string, as every compute provider has different attributes schema
        /// </summary>
        [Input("computeAttributes")]
        public Input<string>? ComputeAttributes { get; set; }

        [Input("computeProfileId")]
        public Input<int>? ComputeProfileId { get; set; }

        [Input("computeResourceId")]
        public Input<int>? ComputeResourceId { get; set; }

        [Input("configGroupIds")]
        private InputList<int>? _configGroupIds;

        /// <summary>
        /// IDs of the applied config groups.
        /// </summary>
        public InputList<int> ConfigGroupIds
        {
            get => _configGroupIds ?? (_configGroupIds = new InputList<int>());
            set => _configGroupIds = value;
        }

        /// <summary>
        /// ID of the domain to assign to the host.
        /// </summary>
        [Input("domainId")]
        public Input<int>? DomainId { get; set; }

        /// <summary>
        /// Enables PMI/BMC functionality. On create and update calls, having this enabled will force a host to poweroff, set next
        /// boot to PXE and power on. Defaults to `false`.
        /// </summary>
        [Input("enableBmc")]
        public Input<bool>? EnableBmc { get; set; }

        /// <summary>
        /// ID of the environment to assign to the host.
        /// </summary>
        [Input("environmentId")]
        public Input<int>? EnvironmentId { get; set; }

        /// <summary>
        /// ID of the hostgroup to assign to the host.
        /// </summary>
        [Input("hostgroupId")]
        public Input<int>? HostgroupId { get; set; }

        /// <summary>
        /// ID of an image to be used as base for this host when cloning
        /// </summary>
        [Input("imageId")]
        public Input<int>? ImageId { get; set; }

        [Input("interfacesAttributes")]
        private InputList<Inputs.HostInterfacesAttributeArgs>? _interfacesAttributes;

        /// <summary>
        /// Host interface information.
        /// </summary>
        public InputList<Inputs.HostInterfacesAttributeArgs> InterfacesAttributes
        {
            get => _interfacesAttributes ?? (_interfacesAttributes = new InputList<Inputs.HostInterfacesAttributeArgs>());
            set => _interfacesAttributes = value;
        }

        /// <summary>
        /// Manage power operations, e.g. power on, if host's build flag will be enabled.
        /// </summary>
        [Input("managePowerOperations")]
        public Input<bool>? ManagePowerOperations { get; set; }

        /// <summary>
        /// Whether or not this host is managed by Foreman. Create host only, don't set build status or manage power states.
        /// </summary>
        [Input("managed")]
        public Input<bool>? Managed { get; set; }

        /// <summary>
        /// ID of the medium mounted on the host.
        /// </summary>
        [Input("mediumId")]
        public Input<int>? MediumId { get; set; }

        /// <summary>
        /// ID of the hardware model if applicable
        /// </summary>
        [Input("modelId")]
        public Input<int>? ModelId { get; set; }

        /// <summary>
        /// Name of this host as stored in Foreman. Can be short name or FQDN, depending on your Foreman settings (especially the
        /// setting 'append_domain_name_for_hosts').
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// ID of the operating system to put on the host.
        /// </summary>
        [Input("operatingsystemId")]
        public Input<int>? OperatingsystemId { get; set; }

        /// <summary>
        /// ID of the user or usergroup that owns the host.
        /// </summary>
        [Input("ownerId")]
        public Input<int>? OwnerId { get; set; }

        /// <summary>
        /// Owner of the host, must be either User ot Usergroup
        /// </summary>
        [Input("ownerType")]
        public Input<string>? OwnerType { get; set; }

        [Input("parameters")]
        private InputMap<string>? _parameters;

        /// <summary>
        /// A map of parameters that will be saved as host parameters in the machine config.
        /// </summary>
        public InputMap<string> Parameters
        {
            get => _parameters ?? (_parameters = new InputMap<string>());
            set => _parameters = value;
        }

        /// <summary>
        /// Sets the provision method in Foreman for this host: either network-based ('build') or image-based ('image')
        /// </summary>
        [Input("provisionMethod")]
        public Input<string>? ProvisionMethod { get; set; }

        /// <summary>
        /// ID of the partition table the host should use
        /// </summary>
        [Input("ptableId")]
        public Input<int>? PtableId { get; set; }

        [Input("puppetClassIds")]
        private InputList<int>? _puppetClassIds;

        /// <summary>
        /// IDs of the applied puppet classes.
        /// </summary>
        public InputList<int> PuppetClassIds
        {
            get => _puppetClassIds ?? (_puppetClassIds = new InputList<int>());
            set => _puppetClassIds = value;
        }

        /// <summary>
        /// Number of times to retry on a failed attempt to register or delete a host in foreman.
        /// </summary>
        [Input("retryCount")]
        public Input<int>? RetryCount { get; set; }

        [Input("rootPassword")]
        private Input<string>? _rootPassword;

        /// <summary>
        /// Default root password
        /// </summary>
        public Input<string>? RootPassword
        {
            get => _rootPassword;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _rootPassword = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Sets the Foreman-internal 'build' flag on this host - even if it is already built completely.
        /// </summary>
        [Input("setBuildFlag")]
        public Input<bool>? SetBuildFlag { get; set; }

        /// <summary>
        /// The short name of this host. Example: when the FQDN is 'host01.example.org', then 'host01' is the short name.
        /// </summary>
        [Input("shortname")]
        public Input<string>? Shortname { get; set; }

        /// <summary>
        /// ID of the subnet the host should be placed in
        /// </summary>
        [Input("subnetId")]
        public Input<int>? SubnetId { get; set; }

        public HostArgs()
        {
        }
        public static new HostArgs Empty => new HostArgs();
    }

    public sealed class HostState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// @SUMMARY A host managed by Foreman.
        /// </summary>
        [Input("__meta_")]
        public Input<bool>? __meta_ { get; set; }

        /// <summary>
        /// ID of the architecture of this host
        /// </summary>
        [Input("architectureId")]
        public Input<int>? ArchitectureId { get; set; }

        [Input("bmcSuccess")]
        public Input<bool>? BmcSuccess { get; set; }

        /// <summary>
        /// Add additional information about this host.Note: Changes to this attribute will trigger a host rebuild.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// Hypervisor specific VM options. Must be a JSON string, as every compute provider has different attributes schema
        /// </summary>
        [Input("computeAttributes")]
        public Input<string>? ComputeAttributes { get; set; }

        [Input("computeProfileId")]
        public Input<int>? ComputeProfileId { get; set; }

        [Input("computeResourceId")]
        public Input<int>? ComputeResourceId { get; set; }

        [Input("configGroupIds")]
        private InputList<int>? _configGroupIds;

        /// <summary>
        /// IDs of the applied config groups.
        /// </summary>
        public InputList<int> ConfigGroupIds
        {
            get => _configGroupIds ?? (_configGroupIds = new InputList<int>());
            set => _configGroupIds = value;
        }

        /// <summary>
        /// ID of the domain to assign to the host.
        /// </summary>
        [Input("domainId")]
        public Input<int>? DomainId { get; set; }

        /// <summary>
        /// The domain name of the host.
        /// </summary>
        [Input("domainName")]
        public Input<string>? DomainName { get; set; }

        /// <summary>
        /// Enables PMI/BMC functionality. On create and update calls, having this enabled will force a host to poweroff, set next
        /// boot to PXE and power on. Defaults to `false`.
        /// </summary>
        [Input("enableBmc")]
        public Input<bool>? EnableBmc { get; set; }

        /// <summary>
        /// ID of the environment to assign to the host.
        /// </summary>
        [Input("environmentId")]
        public Input<int>? EnvironmentId { get; set; }

        /// <summary>
        /// Host fully qualified domain name. Read-only value to be used in variables. @EXAMPLE "compute01.dc1.company.com"
        /// </summary>
        [Input("fqdn")]
        public Input<string>? Fqdn { get; set; }

        /// <summary>
        /// ID of the hostgroup to assign to the host.
        /// </summary>
        [Input("hostgroupId")]
        public Input<int>? HostgroupId { get; set; }

        /// <summary>
        /// ID of an image to be used as base for this host when cloning
        /// </summary>
        [Input("imageId")]
        public Input<int>? ImageId { get; set; }

        [Input("interfacesAttributes")]
        private InputList<Inputs.HostInterfacesAttributeGetArgs>? _interfacesAttributes;

        /// <summary>
        /// Host interface information.
        /// </summary>
        public InputList<Inputs.HostInterfacesAttributeGetArgs> InterfacesAttributes
        {
            get => _interfacesAttributes ?? (_interfacesAttributes = new InputList<Inputs.HostInterfacesAttributeGetArgs>());
            set => _interfacesAttributes = value;
        }

        /// <summary>
        /// Manage power operations, e.g. power on, if host's build flag will be enabled.
        /// </summary>
        [Input("managePowerOperations")]
        public Input<bool>? ManagePowerOperations { get; set; }

        /// <summary>
        /// Whether or not this host is managed by Foreman. Create host only, don't set build status or manage power states.
        /// </summary>
        [Input("managed")]
        public Input<bool>? Managed { get; set; }

        /// <summary>
        /// ID of the medium mounted on the host.
        /// </summary>
        [Input("mediumId")]
        public Input<int>? MediumId { get; set; }

        /// <summary>
        /// ID of the hardware model if applicable
        /// </summary>
        [Input("modelId")]
        public Input<int>? ModelId { get; set; }

        /// <summary>
        /// Name of this host as stored in Foreman. Can be short name or FQDN, depending on your Foreman settings (especially the
        /// setting 'append_domain_name_for_hosts').
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// ID of the operating system to put on the host.
        /// </summary>
        [Input("operatingsystemId")]
        public Input<int>? OperatingsystemId { get; set; }

        /// <summary>
        /// ID of the user or usergroup that owns the host.
        /// </summary>
        [Input("ownerId")]
        public Input<int>? OwnerId { get; set; }

        /// <summary>
        /// Owner of the host, must be either User ot Usergroup
        /// </summary>
        [Input("ownerType")]
        public Input<string>? OwnerType { get; set; }

        [Input("parameters")]
        private InputMap<string>? _parameters;

        /// <summary>
        /// A map of parameters that will be saved as host parameters in the machine config.
        /// </summary>
        public InputMap<string> Parameters
        {
            get => _parameters ?? (_parameters = new InputMap<string>());
            set => _parameters = value;
        }

        /// <summary>
        /// Sets the provision method in Foreman for this host: either network-based ('build') or image-based ('image')
        /// </summary>
        [Input("provisionMethod")]
        public Input<string>? ProvisionMethod { get; set; }

        /// <summary>
        /// ID of the partition table the host should use
        /// </summary>
        [Input("ptableId")]
        public Input<int>? PtableId { get; set; }

        [Input("puppetClassIds")]
        private InputList<int>? _puppetClassIds;

        /// <summary>
        /// IDs of the applied puppet classes.
        /// </summary>
        public InputList<int> PuppetClassIds
        {
            get => _puppetClassIds ?? (_puppetClassIds = new InputList<int>());
            set => _puppetClassIds = value;
        }

        /// <summary>
        /// Number of times to retry on a failed attempt to register or delete a host in foreman.
        /// </summary>
        [Input("retryCount")]
        public Input<int>? RetryCount { get; set; }

        [Input("rootPassword")]
        private Input<string>? _rootPassword;

        /// <summary>
        /// Default root password
        /// </summary>
        public Input<string>? RootPassword
        {
            get => _rootPassword;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _rootPassword = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Sets the Foreman-internal 'build' flag on this host - even if it is already built completely.
        /// </summary>
        [Input("setBuildFlag")]
        public Input<bool>? SetBuildFlag { get; set; }

        /// <summary>
        /// The short name of this host. Example: when the FQDN is 'host01.example.org', then 'host01' is the short name.
        /// </summary>
        [Input("shortname")]
        public Input<string>? Shortname { get; set; }

        /// <summary>
        /// ID of the subnet the host should be placed in
        /// </summary>
        [Input("subnetId")]
        public Input<int>? SubnetId { get; set; }

        /// <summary>
        /// Build token. Can be used to signal to Foreman that a host build is complete.
        /// </summary>
        [Input("token")]
        public Input<string>? Token { get; set; }

        public HostState()
        {
        }
        public static new HostState Empty => new HostState();
    }
}
