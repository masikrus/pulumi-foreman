// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman.Inputs
{

    public sealed class ComputeprofileComputeAttributeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the compute resource
        /// </summary>
        [Input("computeResourceId", required: true)]
        public Input<int> ComputeResourceId { get; set; } = null!;

        /// <summary>
        /// ID of the compute_attribute
        /// </summary>
        [Input("id")]
        public Input<int>? Id { get; set; }

        /// <summary>
        /// Auto-generated name of the compute attribute
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("vmAttrs")]
        private InputMap<string>? _vmAttrs;

        /// <summary>
        /// VM attributes as JSON
        /// </summary>
        public InputMap<string> VmAttrs
        {
            get => _vmAttrs ?? (_vmAttrs = new InputMap<string>());
            set => _vmAttrs = value;
        }

        public ComputeprofileComputeAttributeArgs()
        {
        }
        public static new ComputeprofileComputeAttributeArgs Empty => new ComputeprofileComputeAttributeArgs();
    }
}
