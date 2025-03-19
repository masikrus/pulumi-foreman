// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"errors"
	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Jobtemplate struct {
	pulumi.CustomResourceState

	// @SUMMARY Foreman representation of a job template.
	__meta_           pulumi.BoolOutput      `pulumi:"__meta_"`
	Description       pulumi.StringPtrOutput `pulumi:"description"`
	DescriptionFormat pulumi.StringPtrOutput `pulumi:"descriptionFormat"`
	JobCategory       pulumi.StringOutput    `pulumi:"jobCategory"`
	Locked            pulumi.BoolPtrOutput   `pulumi:"locked"`
	// The name of the job template
	Name         pulumi.StringOutput    `pulumi:"name"`
	ProviderType pulumi.StringPtrOutput `pulumi:"providerType"`
	Snippet      pulumi.BoolPtrOutput   `pulumi:"snippet"`
	// The template content itself
	Template       pulumi.StringOutput                 `pulumi:"template"`
	TemplateInputs JobtemplateTemplateInputArrayOutput `pulumi:"templateInputs"`
}

// NewJobtemplate registers a new resource with the given unique name, arguments, and options.
func NewJobtemplate(ctx *pulumi.Context,
	name string, args *JobtemplateArgs, opts ...pulumi.ResourceOption) (*Jobtemplate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.JobCategory == nil {
		return nil, errors.New("invalid value for required argument 'JobCategory'")
	}
	if args.Template == nil {
		return nil, errors.New("invalid value for required argument 'Template'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Jobtemplate
	err := ctx.RegisterResource("foreman:index/jobtemplate:Jobtemplate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetJobtemplate gets an existing Jobtemplate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetJobtemplate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *JobtemplateState, opts ...pulumi.ResourceOption) (*Jobtemplate, error) {
	var resource Jobtemplate
	err := ctx.ReadResource("foreman:index/jobtemplate:Jobtemplate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Jobtemplate resources.
type jobtemplateState struct {
	// @SUMMARY Foreman representation of a job template.
	__meta_           *bool   `pulumi:"__meta_"`
	Description       *string `pulumi:"description"`
	DescriptionFormat *string `pulumi:"descriptionFormat"`
	JobCategory       *string `pulumi:"jobCategory"`
	Locked            *bool   `pulumi:"locked"`
	// The name of the job template
	Name         *string `pulumi:"name"`
	ProviderType *string `pulumi:"providerType"`
	Snippet      *bool   `pulumi:"snippet"`
	// The template content itself
	Template       *string                    `pulumi:"template"`
	TemplateInputs []JobtemplateTemplateInput `pulumi:"templateInputs"`
}

type JobtemplateState struct {
	// @SUMMARY Foreman representation of a job template.
	__meta_           pulumi.BoolPtrInput
	Description       pulumi.StringPtrInput
	DescriptionFormat pulumi.StringPtrInput
	JobCategory       pulumi.StringPtrInput
	Locked            pulumi.BoolPtrInput
	// The name of the job template
	Name         pulumi.StringPtrInput
	ProviderType pulumi.StringPtrInput
	Snippet      pulumi.BoolPtrInput
	// The template content itself
	Template       pulumi.StringPtrInput
	TemplateInputs JobtemplateTemplateInputArrayInput
}

func (JobtemplateState) ElementType() reflect.Type {
	return reflect.TypeOf((*jobtemplateState)(nil)).Elem()
}

type jobtemplateArgs struct {
	Description       *string `pulumi:"description"`
	DescriptionFormat *string `pulumi:"descriptionFormat"`
	JobCategory       string  `pulumi:"jobCategory"`
	Locked            *bool   `pulumi:"locked"`
	// The name of the job template
	Name         *string `pulumi:"name"`
	ProviderType *string `pulumi:"providerType"`
	Snippet      *bool   `pulumi:"snippet"`
	// The template content itself
	Template       string                     `pulumi:"template"`
	TemplateInputs []JobtemplateTemplateInput `pulumi:"templateInputs"`
}

// The set of arguments for constructing a Jobtemplate resource.
type JobtemplateArgs struct {
	Description       pulumi.StringPtrInput
	DescriptionFormat pulumi.StringPtrInput
	JobCategory       pulumi.StringInput
	Locked            pulumi.BoolPtrInput
	// The name of the job template
	Name         pulumi.StringPtrInput
	ProviderType pulumi.StringPtrInput
	Snippet      pulumi.BoolPtrInput
	// The template content itself
	Template       pulumi.StringInput
	TemplateInputs JobtemplateTemplateInputArrayInput
}

func (JobtemplateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*jobtemplateArgs)(nil)).Elem()
}

type JobtemplateInput interface {
	pulumi.Input

	ToJobtemplateOutput() JobtemplateOutput
	ToJobtemplateOutputWithContext(ctx context.Context) JobtemplateOutput
}

func (*Jobtemplate) ElementType() reflect.Type {
	return reflect.TypeOf((**Jobtemplate)(nil)).Elem()
}

func (i *Jobtemplate) ToJobtemplateOutput() JobtemplateOutput {
	return i.ToJobtemplateOutputWithContext(context.Background())
}

func (i *Jobtemplate) ToJobtemplateOutputWithContext(ctx context.Context) JobtemplateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(JobtemplateOutput)
}

// JobtemplateArrayInput is an input type that accepts JobtemplateArray and JobtemplateArrayOutput values.
// You can construct a concrete instance of `JobtemplateArrayInput` via:
//
//	JobtemplateArray{ JobtemplateArgs{...} }
type JobtemplateArrayInput interface {
	pulumi.Input

	ToJobtemplateArrayOutput() JobtemplateArrayOutput
	ToJobtemplateArrayOutputWithContext(context.Context) JobtemplateArrayOutput
}

type JobtemplateArray []JobtemplateInput

func (JobtemplateArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Jobtemplate)(nil)).Elem()
}

func (i JobtemplateArray) ToJobtemplateArrayOutput() JobtemplateArrayOutput {
	return i.ToJobtemplateArrayOutputWithContext(context.Background())
}

func (i JobtemplateArray) ToJobtemplateArrayOutputWithContext(ctx context.Context) JobtemplateArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(JobtemplateArrayOutput)
}

// JobtemplateMapInput is an input type that accepts JobtemplateMap and JobtemplateMapOutput values.
// You can construct a concrete instance of `JobtemplateMapInput` via:
//
//	JobtemplateMap{ "key": JobtemplateArgs{...} }
type JobtemplateMapInput interface {
	pulumi.Input

	ToJobtemplateMapOutput() JobtemplateMapOutput
	ToJobtemplateMapOutputWithContext(context.Context) JobtemplateMapOutput
}

type JobtemplateMap map[string]JobtemplateInput

func (JobtemplateMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Jobtemplate)(nil)).Elem()
}

func (i JobtemplateMap) ToJobtemplateMapOutput() JobtemplateMapOutput {
	return i.ToJobtemplateMapOutputWithContext(context.Background())
}

func (i JobtemplateMap) ToJobtemplateMapOutputWithContext(ctx context.Context) JobtemplateMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(JobtemplateMapOutput)
}

type JobtemplateOutput struct{ *pulumi.OutputState }

func (JobtemplateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Jobtemplate)(nil)).Elem()
}

func (o JobtemplateOutput) ToJobtemplateOutput() JobtemplateOutput {
	return o
}

func (o JobtemplateOutput) ToJobtemplateOutputWithContext(ctx context.Context) JobtemplateOutput {
	return o
}

// @SUMMARY Foreman representation of a job template.
func (o JobtemplateOutput) __meta_() pulumi.BoolOutput {
	return o.ApplyT(func(v *Jobtemplate) pulumi.BoolOutput { return v.__meta_ }).(pulumi.BoolOutput)
}

func (o JobtemplateOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Jobtemplate) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o JobtemplateOutput) DescriptionFormat() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Jobtemplate) pulumi.StringPtrOutput { return v.DescriptionFormat }).(pulumi.StringPtrOutput)
}

func (o JobtemplateOutput) JobCategory() pulumi.StringOutput {
	return o.ApplyT(func(v *Jobtemplate) pulumi.StringOutput { return v.JobCategory }).(pulumi.StringOutput)
}

func (o JobtemplateOutput) Locked() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Jobtemplate) pulumi.BoolPtrOutput { return v.Locked }).(pulumi.BoolPtrOutput)
}

// The name of the job template
func (o JobtemplateOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Jobtemplate) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o JobtemplateOutput) ProviderType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Jobtemplate) pulumi.StringPtrOutput { return v.ProviderType }).(pulumi.StringPtrOutput)
}

func (o JobtemplateOutput) Snippet() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Jobtemplate) pulumi.BoolPtrOutput { return v.Snippet }).(pulumi.BoolPtrOutput)
}

// The template content itself
func (o JobtemplateOutput) Template() pulumi.StringOutput {
	return o.ApplyT(func(v *Jobtemplate) pulumi.StringOutput { return v.Template }).(pulumi.StringOutput)
}

func (o JobtemplateOutput) TemplateInputs() JobtemplateTemplateInputArrayOutput {
	return o.ApplyT(func(v *Jobtemplate) JobtemplateTemplateInputArrayOutput { return v.TemplateInputs }).(JobtemplateTemplateInputArrayOutput)
}

type JobtemplateArrayOutput struct{ *pulumi.OutputState }

func (JobtemplateArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Jobtemplate)(nil)).Elem()
}

func (o JobtemplateArrayOutput) ToJobtemplateArrayOutput() JobtemplateArrayOutput {
	return o
}

func (o JobtemplateArrayOutput) ToJobtemplateArrayOutputWithContext(ctx context.Context) JobtemplateArrayOutput {
	return o
}

func (o JobtemplateArrayOutput) Index(i pulumi.IntInput) JobtemplateOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Jobtemplate {
		return vs[0].([]*Jobtemplate)[vs[1].(int)]
	}).(JobtemplateOutput)
}

type JobtemplateMapOutput struct{ *pulumi.OutputState }

func (JobtemplateMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Jobtemplate)(nil)).Elem()
}

func (o JobtemplateMapOutput) ToJobtemplateMapOutput() JobtemplateMapOutput {
	return o
}

func (o JobtemplateMapOutput) ToJobtemplateMapOutputWithContext(ctx context.Context) JobtemplateMapOutput {
	return o
}

func (o JobtemplateMapOutput) MapIndex(k pulumi.StringInput) JobtemplateOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Jobtemplate {
		return vs[0].(map[string]*Jobtemplate)[vs[1].(string)]
	}).(JobtemplateOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*JobtemplateInput)(nil)).Elem(), &Jobtemplate{})
	pulumi.RegisterInputType(reflect.TypeOf((*JobtemplateArrayInput)(nil)).Elem(), JobtemplateArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*JobtemplateMapInput)(nil)).Elem(), JobtemplateMap{})
	pulumi.RegisterOutputType(JobtemplateOutput{})
	pulumi.RegisterOutputType(JobtemplateArrayOutput{})
	pulumi.RegisterOutputType(JobtemplateMapOutput{})
}
