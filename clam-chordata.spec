Name: clam-chordata
Version: 1.0.0
Release: 1
Summary: A chord detection tool
URL: https://clam-project.org/
Group: Sound
License: GPL
Source: http://clam-project.org/download/src/chordata-%{version}.tar.gz
BuildRequires: scons libclam-devel qt4-devel libclam-qtmonitors-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
CLAM Chordata is a chord detection tool that can be used to browse the
chords of your favourite mp3/ogg/wav music. You can freely move around the
song, listening and getting insight of its tonal features by using several
available views: Chord segments, Chord ranking, Tonnetz, Keyspace, Chromatic
peaks, PCPgram and others.

%prep
%setup -q -n chordata-%{version}

%build
mkdir -p %{buildroot}%{_prefix}
scons \
  prefix=%{buildroot}%{_prefix} \
  clam_prefix=%{_prefix} \
  release=yes

%install
mkdir -p %{buildroot}%{_prefix}
scons install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/chordata
%{_datadir}/applications/Chordata.desktop
%{_mandir}/man1/chordata.1*
