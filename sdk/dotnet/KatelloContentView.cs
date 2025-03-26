// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Foreman
{
    [ForemanResourceType("foreman:index/katelloContentView:KatelloContentView")]
    public partial class KatelloContentView : global::Pulumi.CustomResource
    {
        /// <summary>
        /// @SUMMARY (Composite) Content Views create an abstract view on a collection of repositories and allow versioning of these
        /// views. Additional fine tuning can be done with package filters.
        /// </summary>
        [Output("__meta_")]
        public Output<bool> __meta_ { get; private set; } = null!;

        /// <summary>
        /// Relevant for Composite Content Views: 'Automatically publish a new version of the composite content view whenever one of
        /// its content views is published. Autopublish will only happen for component views that use the 'Always use latest
        /// version' option.'
        /// </summary>
        [Output("autoPublish")]
        public Output<bool?> AutoPublish { get; private set; } = null!;

        /// <summary>
        /// Relevant for CCVs: list of CV version IDs. @EXAMPLE [1, 4]
        /// </summary>
        [Output("componentIds")]
        public Output<ImmutableArray<int>> ComponentIds { get; private set; } = null!;

        /// <summary>
        /// Is this Content View a Composite CV? @EXAMPLE false
        /// </summary>
        [Output("composite")]
        public Output<bool?> Composite { get; private set; } = null!;

        /// <summary>
        /// Description for the (composite) content view
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("filtered")]
        public Output<bool> Filtered { get; private set; } = null!;

        /// <summary>
        /// Content view filters and their rules.
        /// </summary>
        [Output("filters")]
        public Output<ImmutableArray<Outputs.KatelloContentViewFilter>> Filters { get; private set; } = null!;

        /// <summary>
        /// Label for the (composite) content view. Cannot be changed after creation. By default set to the name, with underscores
        /// as spaces replacement. @EXAMPLE
        /// </summary>
        [Output("label")]
        public Output<string> Label { get; private set; } = null!;

        /// <summary>
        /// Holds the ID of the latest published version of a Content View to be used as reference in CCVs
        /// </summary>
        [Output("latestVersionId")]
        public Output<int> LatestVersionId { get; private set; } = null!;

        /// <summary>
        /// Name of the (composite) content view. @EXAMPLE "My new CV"
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("organizationId")]
        public Output<int> OrganizationId { get; private set; } = null!;

        /// <summary>
        /// List of repository IDs. @EXAMPLE [1, 4, 5]
        /// </summary>
        [Output("repositoryIds")]
        public Output<ImmutableArray<int>> RepositoryIds { get; private set; } = null!;

        /// <summary>
        /// Relevant for Content Views: 'This will solve RPM and module stream dependencies on every publish of this content view.
        /// Dependency solving significantly increases publish time (publishes can take over three times as long) and filters will
        /// be ignored when adding packages to solve dependencies. Also, certain scenarios involving errata may still cause
        /// dependency errors.'
        /// </summary>
        [Output("solveDependencies")]
        public Output<bool?> SolveDependencies { get; private set; } = null!;


        /// <summary>
        /// Create a KatelloContentView resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public KatelloContentView(string name, KatelloContentViewArgs? args = null, CustomResourceOptions? options = null)
            : base("foreman:index/katelloContentView:KatelloContentView", name, args ?? new KatelloContentViewArgs(), MakeResourceOptions(options, ""))
        {
        }

        private KatelloContentView(string name, Input<string> id, KatelloContentViewState? state = null, CustomResourceOptions? options = null)
            : base("foreman:index/katelloContentView:KatelloContentView", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing KatelloContentView resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static KatelloContentView Get(string name, Input<string> id, KatelloContentViewState? state = null, CustomResourceOptions? options = null)
        {
            return new KatelloContentView(name, id, state, options);
        }
    }

    public sealed class KatelloContentViewArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Relevant for Composite Content Views: 'Automatically publish a new version of the composite content view whenever one of
        /// its content views is published. Autopublish will only happen for component views that use the 'Always use latest
        /// version' option.'
        /// </summary>
        [Input("autoPublish")]
        public Input<bool>? AutoPublish { get; set; }

        [Input("componentIds")]
        private InputList<int>? _componentIds;

        /// <summary>
        /// Relevant for CCVs: list of CV version IDs. @EXAMPLE [1, 4]
        /// </summary>
        public InputList<int> ComponentIds
        {
            get => _componentIds ?? (_componentIds = new InputList<int>());
            set => _componentIds = value;
        }

        /// <summary>
        /// Is this Content View a Composite CV? @EXAMPLE false
        /// </summary>
        [Input("composite")]
        public Input<bool>? Composite { get; set; }

        /// <summary>
        /// Description for the (composite) content view
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("filters")]
        private InputList<Inputs.KatelloContentViewFilterArgs>? _filters;

        /// <summary>
        /// Content view filters and their rules.
        /// </summary>
        public InputList<Inputs.KatelloContentViewFilterArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.KatelloContentViewFilterArgs>());
            set => _filters = value;
        }

        /// <summary>
        /// Label for the (composite) content view. Cannot be changed after creation. By default set to the name, with underscores
        /// as spaces replacement. @EXAMPLE
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// Name of the (composite) content view. @EXAMPLE "My new CV"
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("organizationId")]
        public Input<int>? OrganizationId { get; set; }

        [Input("repositoryIds")]
        private InputList<int>? _repositoryIds;

        /// <summary>
        /// List of repository IDs. @EXAMPLE [1, 4, 5]
        /// </summary>
        public InputList<int> RepositoryIds
        {
            get => _repositoryIds ?? (_repositoryIds = new InputList<int>());
            set => _repositoryIds = value;
        }

        /// <summary>
        /// Relevant for Content Views: 'This will solve RPM and module stream dependencies on every publish of this content view.
        /// Dependency solving significantly increases publish time (publishes can take over three times as long) and filters will
        /// be ignored when adding packages to solve dependencies. Also, certain scenarios involving errata may still cause
        /// dependency errors.'
        /// </summary>
        [Input("solveDependencies")]
        public Input<bool>? SolveDependencies { get; set; }

        public KatelloContentViewArgs()
        {
        }
        public static new KatelloContentViewArgs Empty => new KatelloContentViewArgs();
    }

    public sealed class KatelloContentViewState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// @SUMMARY (Composite) Content Views create an abstract view on a collection of repositories and allow versioning of these
        /// views. Additional fine tuning can be done with package filters.
        /// </summary>
        [Input("__meta_")]
        public Input<bool>? __meta_ { get; set; }

        /// <summary>
        /// Relevant for Composite Content Views: 'Automatically publish a new version of the composite content view whenever one of
        /// its content views is published. Autopublish will only happen for component views that use the 'Always use latest
        /// version' option.'
        /// </summary>
        [Input("autoPublish")]
        public Input<bool>? AutoPublish { get; set; }

        [Input("componentIds")]
        private InputList<int>? _componentIds;

        /// <summary>
        /// Relevant for CCVs: list of CV version IDs. @EXAMPLE [1, 4]
        /// </summary>
        public InputList<int> ComponentIds
        {
            get => _componentIds ?? (_componentIds = new InputList<int>());
            set => _componentIds = value;
        }

        /// <summary>
        /// Is this Content View a Composite CV? @EXAMPLE false
        /// </summary>
        [Input("composite")]
        public Input<bool>? Composite { get; set; }

        /// <summary>
        /// Description for the (composite) content view
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("filtered")]
        public Input<bool>? Filtered { get; set; }

        [Input("filters")]
        private InputList<Inputs.KatelloContentViewFilterGetArgs>? _filters;

        /// <summary>
        /// Content view filters and their rules.
        /// </summary>
        public InputList<Inputs.KatelloContentViewFilterGetArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.KatelloContentViewFilterGetArgs>());
            set => _filters = value;
        }

        /// <summary>
        /// Label for the (composite) content view. Cannot be changed after creation. By default set to the name, with underscores
        /// as spaces replacement. @EXAMPLE
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// Holds the ID of the latest published version of a Content View to be used as reference in CCVs
        /// </summary>
        [Input("latestVersionId")]
        public Input<int>? LatestVersionId { get; set; }

        /// <summary>
        /// Name of the (composite) content view. @EXAMPLE "My new CV"
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("organizationId")]
        public Input<int>? OrganizationId { get; set; }

        [Input("repositoryIds")]
        private InputList<int>? _repositoryIds;

        /// <summary>
        /// List of repository IDs. @EXAMPLE [1, 4, 5]
        /// </summary>
        public InputList<int> RepositoryIds
        {
            get => _repositoryIds ?? (_repositoryIds = new InputList<int>());
            set => _repositoryIds = value;
        }

        /// <summary>
        /// Relevant for Content Views: 'This will solve RPM and module stream dependencies on every publish of this content view.
        /// Dependency solving significantly increases publish time (publishes can take over three times as long) and filters will
        /// be ignored when adding packages to solve dependencies. Also, certain scenarios involving errata may still cause
        /// dependency errors.'
        /// </summary>
        [Input("solveDependencies")]
        public Input<bool>? SolveDependencies { get; set; }

        public KatelloContentViewState()
        {
        }
        public static new KatelloContentViewState Empty => new KatelloContentViewState();
    }
}
