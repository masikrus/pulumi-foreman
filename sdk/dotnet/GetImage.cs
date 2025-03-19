// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    public static class GetImage
    {
        public static Task<GetImageResult> InvokeAsync(GetImageArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetImageResult>("foreman:index/getImage:getImage", args ?? new GetImageArgs(), options.WithDefaults());

        public static Output<GetImageResult> Invoke(GetImageInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetImageResult>("foreman:index/getImage:getImage", args ?? new GetImageInvokeArgs(), options.WithDefaults());

        public static Output<GetImageResult> Invoke(GetImageInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetImageResult>("foreman:index/getImage:getImage", args ?? new GetImageInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetImageArgs : global::Pulumi.InvokeArgs
    {
        [Input("computeResourceId", required: true)]
        public int ComputeResourceId { get; set; }

        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetImageArgs()
        {
        }
        public static new GetImageArgs Empty => new GetImageArgs();
    }

    public sealed class GetImageInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("computeResourceId", required: true)]
        public Input<int> ComputeResourceId { get; set; } = null!;

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetImageInvokeArgs()
        {
        }
        public static new GetImageInvokeArgs Empty => new GetImageInvokeArgs();
    }


    [OutputType]
    public sealed class GetImageResult
    {
        public readonly bool __meta_;
        public readonly int ArchitectureId;
        public readonly int ComputeResourceId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly int OperatingsystemId;
        public readonly bool UserData;
        public readonly string Username;
        public readonly string Uuid;

        [OutputConstructor]
        private GetImageResult(
            bool __meta_,

            int architectureId,

            int computeResourceId,

            string id,

            string name,

            int operatingsystemId,

            bool userData,

            string username,

            string uuid)
        {
            this.__meta_ = __meta_;
            ArchitectureId = architectureId;
            ComputeResourceId = computeResourceId;
            Id = id;
            Name = name;
            OperatingsystemId = operatingsystemId;
            UserData = userData;
            Username = username;
            Uuid = uuid;
        }
    }
}
