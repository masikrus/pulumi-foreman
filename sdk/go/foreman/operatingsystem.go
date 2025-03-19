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

type Operatingsystem struct {
	pulumi.CustomResourceState

	// @SUMMARY Foreman representation of an operating system.
	__meta_ pulumi.BoolOutput `pulumi:"__meta_"`
	// Identifiers of attached architectures
	Architectures pulumi.IntArrayOutput `pulumi:"architectures"`
	// Additional operating system information.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
	// `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
	Family pulumi.StringPtrOutput `pulumi:"family"`
	// Major release version. @EXAMPLE "7"
	Major pulumi.StringOutput `pulumi:"major"`
	// Identifiers of attached media
	Media pulumi.IntArrayOutput `pulumi:"media"`
	// Minor release version. @EXAMPLE "4"
	Minor pulumi.StringPtrOutput `pulumi:"minor"`
	// Operating system name. @EXAMPLE "CentOS"
	Name pulumi.StringOutput `pulumi:"name"`
	// A map of parameters that will be saved as operating system parameters in the os config.
	Parameters pulumi.StringMapOutput `pulumi:"parameters"`
	// Identifiers of attached partition tables
	Partitiontables pulumi.IntArrayOutput `pulumi:"partitiontables"`
	// Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
	PasswordHash pulumi.StringPtrOutput `pulumi:"passwordHash"`
	// Identifiers of attached provisioning templates
	ProvisioningTemplates pulumi.IntArrayOutput `pulumi:"provisioningTemplates"`
	// Code name or release name for the specific operating system version.
	ReleaseName pulumi.StringPtrOutput `pulumi:"releaseName"`
	// The operating system's title is a concatentation of the OS name, major, and minor versions to get a full operating
	// system release.
	Title pulumi.StringOutput `pulumi:"title"`
}

// NewOperatingsystem registers a new resource with the given unique name, arguments, and options.
func NewOperatingsystem(ctx *pulumi.Context,
	name string, args *OperatingsystemArgs, opts ...pulumi.ResourceOption) (*Operatingsystem, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Major == nil {
		return nil, errors.New("invalid value for required argument 'Major'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Operatingsystem
	err := ctx.RegisterResource("foreman:index/operatingsystem:Operatingsystem", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOperatingsystem gets an existing Operatingsystem resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOperatingsystem(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OperatingsystemState, opts ...pulumi.ResourceOption) (*Operatingsystem, error) {
	var resource Operatingsystem
	err := ctx.ReadResource("foreman:index/operatingsystem:Operatingsystem", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Operatingsystem resources.
type operatingsystemState struct {
	// @SUMMARY Foreman representation of an operating system.
	__meta_ *bool `pulumi:"__meta_"`
	// Identifiers of attached architectures
	Architectures []int `pulumi:"architectures"`
	// Additional operating system information.
	Description *string `pulumi:"description"`
	// Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
	// `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
	Family *string `pulumi:"family"`
	// Major release version. @EXAMPLE "7"
	Major *string `pulumi:"major"`
	// Identifiers of attached media
	Media []int `pulumi:"media"`
	// Minor release version. @EXAMPLE "4"
	Minor *string `pulumi:"minor"`
	// Operating system name. @EXAMPLE "CentOS"
	Name *string `pulumi:"name"`
	// A map of parameters that will be saved as operating system parameters in the os config.
	Parameters map[string]string `pulumi:"parameters"`
	// Identifiers of attached partition tables
	Partitiontables []int `pulumi:"partitiontables"`
	// Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
	PasswordHash *string `pulumi:"passwordHash"`
	// Identifiers of attached provisioning templates
	ProvisioningTemplates []int `pulumi:"provisioningTemplates"`
	// Code name or release name for the specific operating system version.
	ReleaseName *string `pulumi:"releaseName"`
	// The operating system's title is a concatentation of the OS name, major, and minor versions to get a full operating
	// system release.
	Title *string `pulumi:"title"`
}

type OperatingsystemState struct {
	// @SUMMARY Foreman representation of an operating system.
	__meta_ pulumi.BoolPtrInput
	// Identifiers of attached architectures
	Architectures pulumi.IntArrayInput
	// Additional operating system information.
	Description pulumi.StringPtrInput
	// Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
	// `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
	Family pulumi.StringPtrInput
	// Major release version. @EXAMPLE "7"
	Major pulumi.StringPtrInput
	// Identifiers of attached media
	Media pulumi.IntArrayInput
	// Minor release version. @EXAMPLE "4"
	Minor pulumi.StringPtrInput
	// Operating system name. @EXAMPLE "CentOS"
	Name pulumi.StringPtrInput
	// A map of parameters that will be saved as operating system parameters in the os config.
	Parameters pulumi.StringMapInput
	// Identifiers of attached partition tables
	Partitiontables pulumi.IntArrayInput
	// Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
	PasswordHash pulumi.StringPtrInput
	// Identifiers of attached provisioning templates
	ProvisioningTemplates pulumi.IntArrayInput
	// Code name or release name for the specific operating system version.
	ReleaseName pulumi.StringPtrInput
	// The operating system's title is a concatentation of the OS name, major, and minor versions to get a full operating
	// system release.
	Title pulumi.StringPtrInput
}

func (OperatingsystemState) ElementType() reflect.Type {
	return reflect.TypeOf((*operatingsystemState)(nil)).Elem()
}

type operatingsystemArgs struct {
	// Identifiers of attached architectures
	Architectures []int `pulumi:"architectures"`
	// Additional operating system information.
	Description *string `pulumi:"description"`
	// Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
	// `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
	Family *string `pulumi:"family"`
	// Major release version. @EXAMPLE "7"
	Major string `pulumi:"major"`
	// Identifiers of attached media
	Media []int `pulumi:"media"`
	// Minor release version. @EXAMPLE "4"
	Minor *string `pulumi:"minor"`
	// Operating system name. @EXAMPLE "CentOS"
	Name *string `pulumi:"name"`
	// A map of parameters that will be saved as operating system parameters in the os config.
	Parameters map[string]string `pulumi:"parameters"`
	// Identifiers of attached partition tables
	Partitiontables []int `pulumi:"partitiontables"`
	// Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
	PasswordHash *string `pulumi:"passwordHash"`
	// Identifiers of attached provisioning templates
	ProvisioningTemplates []int `pulumi:"provisioningTemplates"`
	// Code name or release name for the specific operating system version.
	ReleaseName *string `pulumi:"releaseName"`
}

// The set of arguments for constructing a Operatingsystem resource.
type OperatingsystemArgs struct {
	// Identifiers of attached architectures
	Architectures pulumi.IntArrayInput
	// Additional operating system information.
	Description pulumi.StringPtrInput
	// Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
	// `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
	Family pulumi.StringPtrInput
	// Major release version. @EXAMPLE "7"
	Major pulumi.StringInput
	// Identifiers of attached media
	Media pulumi.IntArrayInput
	// Minor release version. @EXAMPLE "4"
	Minor pulumi.StringPtrInput
	// Operating system name. @EXAMPLE "CentOS"
	Name pulumi.StringPtrInput
	// A map of parameters that will be saved as operating system parameters in the os config.
	Parameters pulumi.StringMapInput
	// Identifiers of attached partition tables
	Partitiontables pulumi.IntArrayInput
	// Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
	PasswordHash pulumi.StringPtrInput
	// Identifiers of attached provisioning templates
	ProvisioningTemplates pulumi.IntArrayInput
	// Code name or release name for the specific operating system version.
	ReleaseName pulumi.StringPtrInput
}

func (OperatingsystemArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*operatingsystemArgs)(nil)).Elem()
}

type OperatingsystemInput interface {
	pulumi.Input

	ToOperatingsystemOutput() OperatingsystemOutput
	ToOperatingsystemOutputWithContext(ctx context.Context) OperatingsystemOutput
}

func (*Operatingsystem) ElementType() reflect.Type {
	return reflect.TypeOf((**Operatingsystem)(nil)).Elem()
}

func (i *Operatingsystem) ToOperatingsystemOutput() OperatingsystemOutput {
	return i.ToOperatingsystemOutputWithContext(context.Background())
}

func (i *Operatingsystem) ToOperatingsystemOutputWithContext(ctx context.Context) OperatingsystemOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OperatingsystemOutput)
}

// OperatingsystemArrayInput is an input type that accepts OperatingsystemArray and OperatingsystemArrayOutput values.
// You can construct a concrete instance of `OperatingsystemArrayInput` via:
//
//	OperatingsystemArray{ OperatingsystemArgs{...} }
type OperatingsystemArrayInput interface {
	pulumi.Input

	ToOperatingsystemArrayOutput() OperatingsystemArrayOutput
	ToOperatingsystemArrayOutputWithContext(context.Context) OperatingsystemArrayOutput
}

type OperatingsystemArray []OperatingsystemInput

func (OperatingsystemArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Operatingsystem)(nil)).Elem()
}

func (i OperatingsystemArray) ToOperatingsystemArrayOutput() OperatingsystemArrayOutput {
	return i.ToOperatingsystemArrayOutputWithContext(context.Background())
}

func (i OperatingsystemArray) ToOperatingsystemArrayOutputWithContext(ctx context.Context) OperatingsystemArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OperatingsystemArrayOutput)
}

// OperatingsystemMapInput is an input type that accepts OperatingsystemMap and OperatingsystemMapOutput values.
// You can construct a concrete instance of `OperatingsystemMapInput` via:
//
//	OperatingsystemMap{ "key": OperatingsystemArgs{...} }
type OperatingsystemMapInput interface {
	pulumi.Input

	ToOperatingsystemMapOutput() OperatingsystemMapOutput
	ToOperatingsystemMapOutputWithContext(context.Context) OperatingsystemMapOutput
}

type OperatingsystemMap map[string]OperatingsystemInput

func (OperatingsystemMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Operatingsystem)(nil)).Elem()
}

func (i OperatingsystemMap) ToOperatingsystemMapOutput() OperatingsystemMapOutput {
	return i.ToOperatingsystemMapOutputWithContext(context.Background())
}

func (i OperatingsystemMap) ToOperatingsystemMapOutputWithContext(ctx context.Context) OperatingsystemMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OperatingsystemMapOutput)
}

type OperatingsystemOutput struct{ *pulumi.OutputState }

func (OperatingsystemOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Operatingsystem)(nil)).Elem()
}

func (o OperatingsystemOutput) ToOperatingsystemOutput() OperatingsystemOutput {
	return o
}

func (o OperatingsystemOutput) ToOperatingsystemOutputWithContext(ctx context.Context) OperatingsystemOutput {
	return o
}

// @SUMMARY Foreman representation of an operating system.
func (o OperatingsystemOutput) __meta_() pulumi.BoolOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.BoolOutput { return v.__meta_ }).(pulumi.BoolOutput)
}

// Identifiers of attached architectures
func (o OperatingsystemOutput) Architectures() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.IntArrayOutput { return v.Architectures }).(pulumi.IntArrayOutput)
}

// Additional operating system information.
func (o OperatingsystemOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Operating system family. Values include: `"AIX"`, `"Altlinux"`, `"Archlinux"`, `"Coreos"`, `"Debian"`, `"Freebsd"`,
// `"Gentoo"`, `"Junos"`, `"NXOS"`, `"Redhat"`, `"Solaris"`, `"Suse"`, `"Windows"`.
func (o OperatingsystemOutput) Family() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.StringPtrOutput { return v.Family }).(pulumi.StringPtrOutput)
}

// Major release version. @EXAMPLE "7"
func (o OperatingsystemOutput) Major() pulumi.StringOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.StringOutput { return v.Major }).(pulumi.StringOutput)
}

// Identifiers of attached media
func (o OperatingsystemOutput) Media() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.IntArrayOutput { return v.Media }).(pulumi.IntArrayOutput)
}

// Minor release version. @EXAMPLE "4"
func (o OperatingsystemOutput) Minor() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.StringPtrOutput { return v.Minor }).(pulumi.StringPtrOutput)
}

// Operating system name. @EXAMPLE "CentOS"
func (o OperatingsystemOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// A map of parameters that will be saved as operating system parameters in the os config.
func (o OperatingsystemOutput) Parameters() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.StringMapOutput { return v.Parameters }).(pulumi.StringMapOutput)
}

// Identifiers of attached partition tables
func (o OperatingsystemOutput) Partitiontables() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.IntArrayOutput { return v.Partitiontables }).(pulumi.IntArrayOutput)
}

// Root password hash function to use. Valid values include: `"MD5"`, `"SHA256"`, `"SHA512"`, `"Base64"`.
func (o OperatingsystemOutput) PasswordHash() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.StringPtrOutput { return v.PasswordHash }).(pulumi.StringPtrOutput)
}

// Identifiers of attached provisioning templates
func (o OperatingsystemOutput) ProvisioningTemplates() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.IntArrayOutput { return v.ProvisioningTemplates }).(pulumi.IntArrayOutput)
}

// Code name or release name for the specific operating system version.
func (o OperatingsystemOutput) ReleaseName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.StringPtrOutput { return v.ReleaseName }).(pulumi.StringPtrOutput)
}

// The operating system's title is a concatentation of the OS name, major, and minor versions to get a full operating
// system release.
func (o OperatingsystemOutput) Title() pulumi.StringOutput {
	return o.ApplyT(func(v *Operatingsystem) pulumi.StringOutput { return v.Title }).(pulumi.StringOutput)
}

type OperatingsystemArrayOutput struct{ *pulumi.OutputState }

func (OperatingsystemArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Operatingsystem)(nil)).Elem()
}

func (o OperatingsystemArrayOutput) ToOperatingsystemArrayOutput() OperatingsystemArrayOutput {
	return o
}

func (o OperatingsystemArrayOutput) ToOperatingsystemArrayOutputWithContext(ctx context.Context) OperatingsystemArrayOutput {
	return o
}

func (o OperatingsystemArrayOutput) Index(i pulumi.IntInput) OperatingsystemOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Operatingsystem {
		return vs[0].([]*Operatingsystem)[vs[1].(int)]
	}).(OperatingsystemOutput)
}

type OperatingsystemMapOutput struct{ *pulumi.OutputState }

func (OperatingsystemMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Operatingsystem)(nil)).Elem()
}

func (o OperatingsystemMapOutput) ToOperatingsystemMapOutput() OperatingsystemMapOutput {
	return o
}

func (o OperatingsystemMapOutput) ToOperatingsystemMapOutputWithContext(ctx context.Context) OperatingsystemMapOutput {
	return o
}

func (o OperatingsystemMapOutput) MapIndex(k pulumi.StringInput) OperatingsystemOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Operatingsystem {
		return vs[0].(map[string]*Operatingsystem)[vs[1].(string)]
	}).(OperatingsystemOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OperatingsystemInput)(nil)).Elem(), &Operatingsystem{})
	pulumi.RegisterInputType(reflect.TypeOf((*OperatingsystemArrayInput)(nil)).Elem(), OperatingsystemArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*OperatingsystemMapInput)(nil)).Elem(), OperatingsystemMap{})
	pulumi.RegisterOutputType(OperatingsystemOutput{})
	pulumi.RegisterOutputType(OperatingsystemArrayOutput{})
	pulumi.RegisterOutputType(OperatingsystemMapOutput{})
}
