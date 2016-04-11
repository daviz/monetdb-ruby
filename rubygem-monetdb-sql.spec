%global gem_name	monetdb-sql

Name:		rubygem-%{gem_name}
Epoch:		1
Version:	1.0
Release:	1%{?dist}
Summary:	Pure Ruby database driver for MonetDB/SQL
Group:		Applications/Databases

License:	MPLv2.0
URL:		http://www.monetdb.org/
Source0:	http://dev.monetdb.org/downloads/ruby/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby >= 1.8.0
BuildArch:	noarch

Requires:	ruby(release)
Requires:	rubygem-bigdecimal

Recommends:	MonetDB-SQL-server5 >= 11.22.0
Suggests:	%{name}-doc = %{version}-%{release}

%description
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains a pure Ruby database driver for MonetDB/SQL.

%package	doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T
cp %{SOURCE0} .


%build
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}/%{gem_dir}

find %{buildroot}%{gem_instdir} -name \*.rb -exec chmod 0644 '{}' +


%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Wed Mar  2 2016 Sjoerd Mullender <sjoerd@acm.org> - 1.0-1
- The Ruby interface to MonetDB is now a separate package.