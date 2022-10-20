Summary:	Graphical class browser for Xt
Name:		viewres
Version:	1.0.7
Release:	1
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xorg-macros)

%description
The viewres program displays a tree showing the widget class hierarchy of the
Athena Widget Set.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%{_bindir}/viewres
%{_datadir}/X11/app-defaults/Viewres
%{_datadir}/X11/app-defaults/Viewres-color
%doc %{_mandir}/man1/viewres.*
