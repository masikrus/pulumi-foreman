// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    public static class GetModel
    {
        public static Task<GetModelResult> InvokeAsync(GetModelArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetModelResult>("foreman:index/getModel:getModel", args ?? new GetModelArgs(), options.WithDefaults());

        public static Output<GetModelResult> Invoke(GetModelInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetModelResult>("foreman:index/getModel:getModel", args ?? new GetModelInvokeArgs(), options.WithDefaults());

        public static Output<GetModelResult> Invoke(GetModelInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetModelResult>("foreman:index/getModel:getModel", args ?? new GetModelInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetModelArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetModelArgs()
        {
        }
        public static new GetModelArgs Empty => new GetModelArgs();
    }

    public sealed class GetModelInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetModelInvokeArgs()
        {
        }
        public static new GetModelInvokeArgs Empty => new GetModelInvokeArgs();
    }


    [OutputType]
    public sealed class GetModelResult
    {
        public readonly bool __meta_;
        public readonly string HardwareModel;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Info;
        public readonly string Name;
        public readonly string VendorClass;

        [OutputConstructor]
        private GetModelResult(
            bool __meta_,

            string hardwareModel,

            string id,

            string info,

            string name,

            string vendorClass)
        {
            this.__meta_ = __meta_;
            HardwareModel = hardwareModel;
            Id = id;
            Info = info;
            Name = name;
            VendorClass = vendorClass;
        }
    }
}
