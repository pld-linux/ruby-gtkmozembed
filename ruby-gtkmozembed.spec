#
# TODO:
#   - subpackages
#
Summary:	Gecko embedded object for Ruby/GNOME2
Summary(pl.UTF-8):	Osadzony obiekt Gecko dla Ruby/GNOME2
Name:		ruby-gtkmozembed
Version:	0.3.1
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/ruby-gnome2/%{name}-%{version}.tar.gz
# Source0-md5:	669b4c8336d987354a3144a6d1d9dd99
URL:		http://ruby-gnome2.sourceforge.jp/
BuildRequires:	mozilla-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-gnome2
BuildRequires:	sed >= 4.0
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gecko embedded object for Ruby/GNOME2.

%description -l pl.UTF-8
Osadzony obiekt Gecko dla Ruby/GNOME2.

%prep
%setup -q

%build
find . -name '*.rb' | xargs sed -i -e '1s,#.*local/bin/ruby,#!%{_bindir}/ruby,'
ruby extconf.rb
%{__make}

rdoc -o rdoc
rdoc --ri -o ri

rm ri/ri/Gtk/cdesc-Gtk.yaml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_rubylibdir},%{ruby_ridir}}
%{__make} install \
	RUBYLIBDIR=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	RUBYARCHDIR=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog rdoc
%attr(755,root,root) %{ruby_archdir}/*.so
%{ruby_rubylibdir}/*.rb
%{ruby_ridir}/*
