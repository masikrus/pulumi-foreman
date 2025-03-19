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

type Computeprofile struct {
	pulumi.CustomResourceState

	// @SUMMARY Foreman representation of a compute profile.
	__meta_ pulumi.BoolOutput `pulumi:"__meta_"`
	// List of compute attributes
	ComputeAttributes ComputeprofileComputeAttributeArrayOutput `pulumi:"computeAttributes"`
	// Name of the compute profile
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewComputeprofile registers a new resource with the given unique name, arguments, and options.
func NewComputeprofile(ctx *pulumi.Context,
	name string, args *ComputeprofileArgs, opts ...pulumi.ResourceOption) (*Computeprofile, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ComputeAttributes == nil {
		return nil, errors.New("invalid value for required argument 'ComputeAttributes'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Computeprofile
	err := ctx.RegisterResource("foreman:index/computeprofile:Computeprofile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetComputeprofile gets an existing Computeprofile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetComputeprofile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ComputeprofileState, opts ...pulumi.ResourceOption) (*Computeprofile, error) {
	var resource Computeprofile
	err := ctx.ReadResource("foreman:index/computeprofile:Computeprofile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Computeprofile resources.
type computeprofileState struct {
	// @SUMMARY Foreman representation of a compute profile.
	__meta_ *bool `pulumi:"__meta_"`
	// List of compute attributes
	ComputeAttributes []ComputeprofileComputeAttribute `pulumi:"computeAttributes"`
	// Name of the compute profile
	Name *string `pulumi:"name"`
}

type ComputeprofileState struct {
	// @SUMMARY Foreman representation of a compute profile.
	__meta_ pulumi.BoolPtrInput
	// List of compute attributes
	ComputeAttributes ComputeprofileComputeAttributeArrayInput
	// Name of the compute profile
	Name pulumi.StringPtrInput
}

func (ComputeprofileState) ElementType() reflect.Type {
	return reflect.TypeOf((*computeprofileState)(nil)).Elem()
}

type computeprofileArgs struct {
	// List of compute attributes
	ComputeAttributes []ComputeprofileComputeAttribute `pulumi:"computeAttributes"`
	// Name of the compute profile
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a Computeprofile resource.
type ComputeprofileArgs struct {
	// List of compute attributes
	ComputeAttributes ComputeprofileComputeAttributeArrayInput
	// Name of the compute profile
	Name pulumi.StringPtrInput
}

func (ComputeprofileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*computeprofileArgs)(nil)).Elem()
}

type ComputeprofileInput interface {
	pulumi.Input

	ToComputeprofileOutput() ComputeprofileOutput
	ToComputeprofileOutputWithContext(ctx context.Context) ComputeprofileOutput
}

func (*Computeprofile) ElementType() reflect.Type {
	return reflect.TypeOf((**Computeprofile)(nil)).Elem()
}

func (i *Computeprofile) ToComputeprofileOutput() ComputeprofileOutput {
	return i.ToComputeprofileOutputWithContext(context.Background())
}

func (i *Computeprofile) ToComputeprofileOutputWithContext(ctx context.Context) ComputeprofileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComputeprofileOutput)
}

// ComputeprofileArrayInput is an input type that accepts ComputeprofileArray and ComputeprofileArrayOutput values.
// You can construct a concrete instance of `ComputeprofileArrayInput` via:
//
//	ComputeprofileArray{ ComputeprofileArgs{...} }
type ComputeprofileArrayInput interface {
	pulumi.Input

	ToComputeprofileArrayOutput() ComputeprofileArrayOutput
	ToComputeprofileArrayOutputWithContext(context.Context) ComputeprofileArrayOutput
}

type ComputeprofileArray []ComputeprofileInput

func (ComputeprofileArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Computeprofile)(nil)).Elem()
}

func (i ComputeprofileArray) ToComputeprofileArrayOutput() ComputeprofileArrayOutput {
	return i.ToComputeprofileArrayOutputWithContext(context.Background())
}

func (i ComputeprofileArray) ToComputeprofileArrayOutputWithContext(ctx context.Context) ComputeprofileArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComputeprofileArrayOutput)
}

// ComputeprofileMapInput is an input type that accepts ComputeprofileMap and ComputeprofileMapOutput values.
// You can construct a concrete instance of `ComputeprofileMapInput` via:
//
//	ComputeprofileMap{ "key": ComputeprofileArgs{...} }
type ComputeprofileMapInput interface {
	pulumi.Input

	ToComputeprofileMapOutput() ComputeprofileMapOutput
	ToComputeprofileMapOutputWithContext(context.Context) ComputeprofileMapOutput
}

type ComputeprofileMap map[string]ComputeprofileInput

func (ComputeprofileMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Computeprofile)(nil)).Elem()
}

func (i ComputeprofileMap) ToComputeprofileMapOutput() ComputeprofileMapOutput {
	return i.ToComputeprofileMapOutputWithContext(context.Background())
}

func (i ComputeprofileMap) ToComputeprofileMapOutputWithContext(ctx context.Context) ComputeprofileMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComputeprofileMapOutput)
}

type ComputeprofileOutput struct{ *pulumi.OutputState }

func (ComputeprofileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Computeprofile)(nil)).Elem()
}

func (o ComputeprofileOutput) ToComputeprofileOutput() ComputeprofileOutput {
	return o
}

func (o ComputeprofileOutput) ToComputeprofileOutputWithContext(ctx context.Context) ComputeprofileOutput {
	return o
}

// @SUMMARY Foreman representation of a compute profile.
func (o ComputeprofileOutput) __meta_() pulumi.BoolOutput {
	return o.ApplyT(func(v *Computeprofile) pulumi.BoolOutput { return v.__meta_ }).(pulumi.BoolOutput)
}

// List of compute attributes
func (o ComputeprofileOutput) ComputeAttributes() ComputeprofileComputeAttributeArrayOutput {
	return o.ApplyT(func(v *Computeprofile) ComputeprofileComputeAttributeArrayOutput { return v.ComputeAttributes }).(ComputeprofileComputeAttributeArrayOutput)
}

// Name of the compute profile
func (o ComputeprofileOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Computeprofile) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

type ComputeprofileArrayOutput struct{ *pulumi.OutputState }

func (ComputeprofileArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Computeprofile)(nil)).Elem()
}

func (o ComputeprofileArrayOutput) ToComputeprofileArrayOutput() ComputeprofileArrayOutput {
	return o
}

func (o ComputeprofileArrayOutput) ToComputeprofileArrayOutputWithContext(ctx context.Context) ComputeprofileArrayOutput {
	return o
}

func (o ComputeprofileArrayOutput) Index(i pulumi.IntInput) ComputeprofileOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Computeprofile {
		return vs[0].([]*Computeprofile)[vs[1].(int)]
	}).(ComputeprofileOutput)
}

type ComputeprofileMapOutput struct{ *pulumi.OutputState }

func (ComputeprofileMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Computeprofile)(nil)).Elem()
}

func (o ComputeprofileMapOutput) ToComputeprofileMapOutput() ComputeprofileMapOutput {
	return o
}

func (o ComputeprofileMapOutput) ToComputeprofileMapOutputWithContext(ctx context.Context) ComputeprofileMapOutput {
	return o
}

func (o ComputeprofileMapOutput) MapIndex(k pulumi.StringInput) ComputeprofileOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Computeprofile {
		return vs[0].(map[string]*Computeprofile)[vs[1].(string)]
	}).(ComputeprofileOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ComputeprofileInput)(nil)).Elem(), &Computeprofile{})
	pulumi.RegisterInputType(reflect.TypeOf((*ComputeprofileArrayInput)(nil)).Elem(), ComputeprofileArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ComputeprofileMapInput)(nil)).Elem(), ComputeprofileMap{})
	pulumi.RegisterOutputType(ComputeprofileOutput{})
	pulumi.RegisterOutputType(ComputeprofileArrayOutput{})
	pulumi.RegisterOutputType(ComputeprofileMapOutput{})
}
