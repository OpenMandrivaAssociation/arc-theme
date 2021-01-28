%global common_configure --with-cinnamon=4.6 --disable-unity --srcdir=..

%global common_desc Arc is a flat theme with transparent elements for GTK 3, GTK 2 and GNOME Shell, Unity, Pantheon, Xfce, MATE, Cinnamon, Budgie Desktop.


Name:		arc-theme
Version:	20210127
Release:	1
Summary:	A flat theme with transparent elements

License:	GPLv3+
URL:		https://github.com/jnsh/arc-theme
Source0:	https://github.com/jnsh/arc-theme/archive/%{version}/arc-theme-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  pkgconf
BuildRequires:	inkscape
BuildRequires:	optipng
BuildRequires:	sassc
BuildRequires:	gnome-shell
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	fdupes
BuildRequires:  make

# as dirty workaround use themes-standard and now broken confliction themes extra
Requires: gnome-themes-standard
#Requires:	gnome-themes-extra
Requires:	murrine

%description
%{common_desc}

%prep
%autosetup -p 1
%{_bindir}/autoreconf -fiv

%build
%{__mkdir} -p regular solid
pushd regular
%{__ln_s} -f ../configure configure
%configure %{common_configure}
popd
pushd solid
%{__ln_s} -f ../configure configure
%configure --disable-transparency %{common_configure}
popd
%make_build -C regular
%make_build -C solid


%install
%make_install -C regular
%make_install -C solid

# Link duplicate files.
%fdupes -s %{buildroot}%{_datadir}


%files
%license AUTHORS COPYING
%doc README.md
%{_datadir}/themes/*
