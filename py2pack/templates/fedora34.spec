#
# spec file for package python-{{ name }}
#
# Copyright (c) {{ year }} {{ user_name }}.
#

Name:           python34-{{ name }}
Version:        {{ version }}
Release:        0
Url:            {{ home_page }}
Summary:        {{ summary }}
{% if license %}
License:        {{ license }}
{% else %}
License:        Unknown 
{% endif %}
Group:          Development/Languages/Python
Source:         {{ source_url|replace(version, '%{version}') }}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      x86_64 
BuildRequires:  python34-devel {%- if requires_python %} = {{ requires_python }} {% endif %}
{%- for req in requires %}
BuildRequires:  python34-{{ req|replace('(','')|replace(')','') }}
Requires:       python34-{{ req|replace('(','')|replace(')','') }}
{%- endfor %}
{%- for req in install_requires %}
BuildRequires:  python34-{{ req|replace('(','')|replace(')','') }}
Requires:       python34-{{ req|replace('(','')|replace(')','') }}
{%- endfor %}
{%- if extras_require %}
{%- for reqlist in extras_require.values() %}
{%- for req in reqlist %}
Suggests:       python34-{{ req|replace('(','')|replace(')','') }}
{%- endfor %}
{%- endfor %}
{%- endif %}

%define _unpackaged_files_terminate_build 0

%description
{{ description }}

%prep
%setup -q -n {{ name }}-%{version}

%build
{%- if is_extension %}
export CFLAGS="%{optflags}"
{%- endif %}
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
{%- if doc_files %}
%doc {{ doc_files|join(" ") }}
{%- endif %}
{%- for script in scripts %}
%{_bindir}/{{ script }}
{%- endfor %}
%{python3_sitearch}/*

%changelog

