// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    [ForemanResourceType("foreman:index/computeprofile:Computeprofile")]
    public partial class Computeprofile : global::Pulumi.CustomResource
    {
        /// <summary>
        /// @SUMMARY Foreman representation of a compute profile.
        /// </summary>
        [Output("__meta_")]
        public Output<bool> __meta_ { get; private set; } = null!;

        /// <summary>
        /// List of compute attributes
        /// </summary>
        [Output("computeAttributes")]
        public Output<ImmutableArray<Outputs.ComputeprofileComputeAttribute>> ComputeAttributes { get; private set; } = null!;

        /// <summary>
        /// Name of the compute profile
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a Computeprofile resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Computeprofile(string name, ComputeprofileArgs args, CustomResourceOptions? options = null)
            : base("foreman:index/computeprofile:Computeprofile", name, args ?? new ComputeprofileArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Computeprofile(string name, Input<string> id, ComputeprofileState? state = null, CustomResourceOptions? options = null)
            : base("foreman:index/computeprofile:Computeprofile", name, state, MakeResourceOptions(options, id))
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
        /// <summary>
        /// Get an existing Computeprofile resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Computeprofile Get(string name, Input<string> id, ComputeprofileState? state = null, CustomResourceOptions? options = null)
        {
            return new Computeprofile(name, id, state, options);
        }
    }

    public sealed class ComputeprofileArgs : global::Pulumi.ResourceArgs
    {
        [Input("computeAttributes", required: true)]
        private InputList<Inputs.ComputeprofileComputeAttributeArgs>? _computeAttributes;

        /// <summary>
        /// List of compute attributes
        /// </summary>
        public InputList<Inputs.ComputeprofileComputeAttributeArgs> ComputeAttributes
        {
            get => _computeAttributes ?? (_computeAttributes = new InputList<Inputs.ComputeprofileComputeAttributeArgs>());
            set => _computeAttributes = value;
        }

        /// <summary>
        /// Name of the compute profile
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ComputeprofileArgs()
        {
        }
        public static new ComputeprofileArgs Empty => new ComputeprofileArgs();
    }

    public sealed class ComputeprofileState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// @SUMMARY Foreman representation of a compute profile.
        /// </summary>
        [Input("__meta_")]
        public Input<bool>? __meta_ { get; set; }

        [Input("computeAttributes")]
        private InputList<Inputs.ComputeprofileComputeAttributeGetArgs>? _computeAttributes;

        /// <summary>
        /// List of compute attributes
        /// </summary>
        public InputList<Inputs.ComputeprofileComputeAttributeGetArgs> ComputeAttributes
        {
            get => _computeAttributes ?? (_computeAttributes = new InputList<Inputs.ComputeprofileComputeAttributeGetArgs>());
            set => _computeAttributes = value;
        }

        /// <summary>
        /// Name of the compute profile
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ComputeprofileState()
        {
        }
        public static new ComputeprofileState Empty => new ComputeprofileState();
    }
}
