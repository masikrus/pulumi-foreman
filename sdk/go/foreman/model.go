// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Model struct {
	pulumi.CustomResourceState

	// @SUMMARY Vendor-specific hardware model.
	__meta_ pulumi.BoolOutput `pulumi:"__meta_"`
	// Name of the specific hardware model.
	HardwareModel pulumi.StringPtrOutput `pulumi:"hardwareModel"`
	// Additional information about this hardware model.
	Info pulumi.StringPtrOutput `pulumi:"info"`
	// The name of the hardware model. @EXAMPLE "PowerEdge FC630"
	Name pulumi.StringOutput `pulumi:"name"`
	// Name or class of the hardware vendor.
	VendorClass pulumi.StringPtrOutput `pulumi:"vendorClass"`
}

// NewModel registers a new resource with the given unique name, arguments, and options.
func NewModel(ctx *pulumi.Context,
	name string, args *ModelArgs, opts ...pulumi.ResourceOption) (*Model, error) {
	if args == nil {
		args = &ModelArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Model
	err := ctx.RegisterResource("foreman:index/model:Model", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetModel gets an existing Model resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetModel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ModelState, opts ...pulumi.ResourceOption) (*Model, error) {
	var resource Model
	err := ctx.ReadResource("foreman:index/model:Model", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Model resources.
type modelState struct {
	// @SUMMARY Vendor-specific hardware model.
	__meta_ *bool `pulumi:"__meta_"`
	// Name of the specific hardware model.
	HardwareModel *string `pulumi:"hardwareModel"`
	// Additional information about this hardware model.
	Info *string `pulumi:"info"`
	// The name of the hardware model. @EXAMPLE "PowerEdge FC630"
	Name *string `pulumi:"name"`
	// Name or class of the hardware vendor.
	VendorClass *string `pulumi:"vendorClass"`
}

type ModelState struct {
	// @SUMMARY Vendor-specific hardware model.
	__meta_ pulumi.BoolPtrInput
	// Name of the specific hardware model.
	HardwareModel pulumi.StringPtrInput
	// Additional information about this hardware model.
	Info pulumi.StringPtrInput
	// The name of the hardware model. @EXAMPLE "PowerEdge FC630"
	Name pulumi.StringPtrInput
	// Name or class of the hardware vendor.
	VendorClass pulumi.StringPtrInput
}

func (ModelState) ElementType() reflect.Type {
	return reflect.TypeOf((*modelState)(nil)).Elem()
}

type modelArgs struct {
	// Name of the specific hardware model.
	HardwareModel *string `pulumi:"hardwareModel"`
	// Additional information about this hardware model.
	Info *string `pulumi:"info"`
	// The name of the hardware model. @EXAMPLE "PowerEdge FC630"
	Name *string `pulumi:"name"`
	// Name or class of the hardware vendor.
	VendorClass *string `pulumi:"vendorClass"`
}

// The set of arguments for constructing a Model resource.
type ModelArgs struct {
	// Name of the specific hardware model.
	HardwareModel pulumi.StringPtrInput
	// Additional information about this hardware model.
	Info pulumi.StringPtrInput
	// The name of the hardware model. @EXAMPLE "PowerEdge FC630"
	Name pulumi.StringPtrInput
	// Name or class of the hardware vendor.
	VendorClass pulumi.StringPtrInput
}

func (ModelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*modelArgs)(nil)).Elem()
}

type ModelInput interface {
	pulumi.Input

	ToModelOutput() ModelOutput
	ToModelOutputWithContext(ctx context.Context) ModelOutput
}

func (*Model) ElementType() reflect.Type {
	return reflect.TypeOf((**Model)(nil)).Elem()
}

func (i *Model) ToModelOutput() ModelOutput {
	return i.ToModelOutputWithContext(context.Background())
}

func (i *Model) ToModelOutputWithContext(ctx context.Context) ModelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelOutput)
}

// ModelArrayInput is an input type that accepts ModelArray and ModelArrayOutput values.
// You can construct a concrete instance of `ModelArrayInput` via:
//
//	ModelArray{ ModelArgs{...} }
type ModelArrayInput interface {
	pulumi.Input

	ToModelArrayOutput() ModelArrayOutput
	ToModelArrayOutputWithContext(context.Context) ModelArrayOutput
}

type ModelArray []ModelInput

func (ModelArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Model)(nil)).Elem()
}

func (i ModelArray) ToModelArrayOutput() ModelArrayOutput {
	return i.ToModelArrayOutputWithContext(context.Background())
}

func (i ModelArray) ToModelArrayOutputWithContext(ctx context.Context) ModelArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelArrayOutput)
}

// ModelMapInput is an input type that accepts ModelMap and ModelMapOutput values.
// You can construct a concrete instance of `ModelMapInput` via:
//
//	ModelMap{ "key": ModelArgs{...} }
type ModelMapInput interface {
	pulumi.Input

	ToModelMapOutput() ModelMapOutput
	ToModelMapOutputWithContext(context.Context) ModelMapOutput
}

type ModelMap map[string]ModelInput

func (ModelMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Model)(nil)).Elem()
}

func (i ModelMap) ToModelMapOutput() ModelMapOutput {
	return i.ToModelMapOutputWithContext(context.Background())
}

func (i ModelMap) ToModelMapOutputWithContext(ctx context.Context) ModelMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelMapOutput)
}

type ModelOutput struct{ *pulumi.OutputState }

func (ModelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Model)(nil)).Elem()
}

func (o ModelOutput) ToModelOutput() ModelOutput {
	return o
}

func (o ModelOutput) ToModelOutputWithContext(ctx context.Context) ModelOutput {
	return o
}

// @SUMMARY Vendor-specific hardware model.
func (o ModelOutput) __meta_() pulumi.BoolOutput {
	return o.ApplyT(func(v *Model) pulumi.BoolOutput { return v.__meta_ }).(pulumi.BoolOutput)
}

// Name of the specific hardware model.
func (o ModelOutput) HardwareModel() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Model) pulumi.StringPtrOutput { return v.HardwareModel }).(pulumi.StringPtrOutput)
}

// Additional information about this hardware model.
func (o ModelOutput) Info() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Model) pulumi.StringPtrOutput { return v.Info }).(pulumi.StringPtrOutput)
}

// The name of the hardware model. @EXAMPLE "PowerEdge FC630"
func (o ModelOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Model) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Name or class of the hardware vendor.
func (o ModelOutput) VendorClass() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Model) pulumi.StringPtrOutput { return v.VendorClass }).(pulumi.StringPtrOutput)
}

type ModelArrayOutput struct{ *pulumi.OutputState }

func (ModelArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Model)(nil)).Elem()
}

func (o ModelArrayOutput) ToModelArrayOutput() ModelArrayOutput {
	return o
}

func (o ModelArrayOutput) ToModelArrayOutputWithContext(ctx context.Context) ModelArrayOutput {
	return o
}

func (o ModelArrayOutput) Index(i pulumi.IntInput) ModelOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Model {
		return vs[0].([]*Model)[vs[1].(int)]
	}).(ModelOutput)
}

type ModelMapOutput struct{ *pulumi.OutputState }

func (ModelMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Model)(nil)).Elem()
}

func (o ModelMapOutput) ToModelMapOutput() ModelMapOutput {
	return o
}

func (o ModelMapOutput) ToModelMapOutputWithContext(ctx context.Context) ModelMapOutput {
	return o
}

func (o ModelMapOutput) MapIndex(k pulumi.StringInput) ModelOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Model {
		return vs[0].(map[string]*Model)[vs[1].(string)]
	}).(ModelOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ModelInput)(nil)).Elem(), &Model{})
	pulumi.RegisterInputType(reflect.TypeOf((*ModelArrayInput)(nil)).Elem(), ModelArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ModelMapInput)(nil)).Elem(), ModelMap{})
	pulumi.RegisterOutputType(ModelOutput{})
	pulumi.RegisterOutputType(ModelArrayOutput{})
	pulumi.RegisterOutputType(ModelMapOutput{})
}
