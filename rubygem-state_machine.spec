# Generated from state_machine-0.9.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	state_machine

Summary:	Adds support for creating state machines for attributes on any Ruby class
Name:		rubygem-%{rbname}

Version:	0.9.4
Release:	2
Group:		Development/Ruby
License:	MIT
URL:		http://www.pluginaweek.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Adds support for creating state machines for attributes on any Ruby class

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f 	'(.*.rb|.*.rdoc|LICENSE|examples|test)'

%install
rm -rf %{buildroot}
%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%{ruby_gemdir}/gems/%{rbname}-%{version}/init.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/examples/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*



%changelog
* Thu Mar 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.9.4-1
+ Revision: 643406
- imported package rubygem-state_machine


* Thu Mar 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.9.4-1
- Initial package
