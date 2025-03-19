// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "foreman:index/architecture:Architecture":
		r = &Architecture{}
	case "foreman:index/computeprofile:Computeprofile":
		r = &Computeprofile{}
	case "foreman:index/computeresource:Computeresource":
		r = &Computeresource{}
	case "foreman:index/defaulttemplate:Defaulttemplate":
		r = &Defaulttemplate{}
	case "foreman:index/domain:Domain":
		r = &Domain{}
	case "foreman:index/environment:Environment":
		r = &Environment{}
	case "foreman:index/globalParameter:GlobalParameter":
		r = &GlobalParameter{}
	case "foreman:index/host:Host":
		r = &Host{}
	case "foreman:index/hostgroup:Hostgroup":
		r = &Hostgroup{}
	case "foreman:index/httpproxy:Httpproxy":
		r = &Httpproxy{}
	case "foreman:index/image:Image":
		r = &Image{}
	case "foreman:index/jobtemplate:Jobtemplate":
		r = &Jobtemplate{}
	case "foreman:index/katelloContentCredential:KatelloContentCredential":
		r = &KatelloContentCredential{}
	case "foreman:index/katelloContentView:KatelloContentView":
		r = &KatelloContentView{}
	case "foreman:index/katelloLifecycleEnvironment:KatelloLifecycleEnvironment":
		r = &KatelloLifecycleEnvironment{}
	case "foreman:index/katelloProduct:KatelloProduct":
		r = &KatelloProduct{}
	case "foreman:index/katelloRepository:KatelloRepository":
		r = &KatelloRepository{}
	case "foreman:index/katelloSyncPlan:KatelloSyncPlan":
		r = &KatelloSyncPlan{}
	case "foreman:index/media:Media":
		r = &Media{}
	case "foreman:index/model:Model":
		r = &Model{}
	case "foreman:index/operatingsystem:Operatingsystem":
		r = &Operatingsystem{}
	case "foreman:index/overrideValue:OverrideValue":
		r = &OverrideValue{}
	case "foreman:index/parameter:Parameter":
		r = &Parameter{}
	case "foreman:index/partitiontable:Partitiontable":
		r = &Partitiontable{}
	case "foreman:index/provisioningtemplate:Provisioningtemplate":
		r = &Provisioningtemplate{}
	case "foreman:index/smartproxy:Smartproxy":
		r = &Smartproxy{}
	case "foreman:index/subnet:Subnet":
		r = &Subnet{}
	case "foreman:index/templateinput:Templateinput":
		r = &Templateinput{}
	case "foreman:index/user:User":
		r = &User{}
	case "foreman:index/usergroup:Usergroup":
		r = &Usergroup{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:foreman" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"foreman",
		"index/architecture",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/computeprofile",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/computeresource",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/defaulttemplate",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/domain",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/environment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/globalParameter",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/host",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/hostgroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/httpproxy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/image",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/jobtemplate",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/katelloContentCredential",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/katelloContentView",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/katelloLifecycleEnvironment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/katelloProduct",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/katelloRepository",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/katelloSyncPlan",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/media",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/model",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/operatingsystem",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/overrideValue",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/parameter",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/partitiontable",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/provisioningtemplate",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/smartproxy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/subnet",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/templateinput",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/user",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"foreman",
		"index/usergroup",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"foreman",
		&pkg{version},
	)
}
