%global common_configure --with-cinnamon=4.6 --disable-unity --srcdir=..

%global common_desc Arc is a flat theme with transparent elements for GTK 3, GTK 2 and GNOME Shell, Unity, Pantheon, Xfce, MATE, Cinnamon, Budgie Desktop.


Name:		arc-theme
Version:	20221218
Release:	2
Summary:	A flat theme with transparent elements

License:	GPLv3+
URL:		https://github.com/jnsh/arc-theme
Source0:	https://github.com/jnsh/arc-theme/archive/%{version}/arc-theme-%{version}.tar.gz

BuildArch:	noarch

BuildRequires: meson
BuildRequires: pkgconf
BuildRequires: inkscape
BuildRequires: optipng
BuildRequires: sassc
BuildRequires: gnome-shell
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: fdupes
BuildRequires: make

# as dirty workaround use themes-standard and now broken confliction themes extra
Requires: gnome-themes-standard
#Requires:	gnome-themes-extra
Requires:	murrine

%description
%{common_desc}

%prep
%autosetup -p 1

%build

%meson \
       -Dthemes=cinnamon,gnome-shell,gtk2,gtk3,gtk4,metacity,plank,xfwm \
       -Dcinnamon_version=5.2
%meson_build 
 
%install
%meson_install

# Link duplicate files.
%fdupes -s %{buildroot}%{_datadir}


%files
%license AUTHORS COPYING
%doc README.md
%{_datadir}/themes/*
