export default function Footer() {
  return (
    <footer className="bg-blue-900 text-white text-center py-4 mt-10">
      &copy; {new Date().getFullYear()} SQL Injection Detector. All rights reserved.
    </footer>
  );
}