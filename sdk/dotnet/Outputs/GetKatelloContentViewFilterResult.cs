// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman.Outputs
{

    [OutputType]
    public sealed class GetKatelloContentViewFilterResult
    {
        public readonly string Description;
        public readonly int Id;
        /// <summary>
        /// specifies if content should be included or excluded, default: inclusion=false
        /// </summary>
        public readonly bool Inclusion;
        public readonly string Name;
        public readonly ImmutableArray<Outputs.GetKatelloContentViewFilterRuleResult> Rules;
        /// <summary>
        /// Type of this filter, e.g. DEB or RPM
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GetKatelloContentViewFilterResult(
            string description,

            int id,

            bool inclusion,

            string name,

            ImmutableArray<Outputs.GetKatelloContentViewFilterRuleResult> rules,

            string type)
        {
            Description = description;
            Id = id;
            Inclusion = inclusion;
            Name = name;
            Rules = rules;
            Type = type;
        }
    }
}
