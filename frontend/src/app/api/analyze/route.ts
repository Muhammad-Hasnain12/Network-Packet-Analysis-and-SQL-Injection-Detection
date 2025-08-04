import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    const formData = await request.formData();
    const file = formData.get('file') as File;
    
    if (!file) {
      return NextResponse.json({ error: 'No file provided' }, { status: 400 });
    }

    // Validate file type
    if (!file.name.endsWith('.pcap') && !file.name.endsWith('.pcapng')) {
      return NextResponse.json({ 
        error: 'Invalid file type. Please upload a .pcap or .pcapng file' 
      }, { status: 400 });
    }

    // Validate file size (max 100MB)
    const maxSize = 100 * 1024 * 1024; // 100MB
    if (file.size > maxSize) {
      return NextResponse.json({ 
        error: 'File too large. Maximum size is 100MB' 
      }, { status: 400 });
    }

    // Simulate processing delay
    await new Promise(resolve => setTimeout(resolve, 2000));

    // Enhanced mock response with more realistic data
    const isDetected = Math.random() > 0.7; // 30% chance of detection for demo
    const mockResult = {
      detected: isDetected,
      details: [
        'Successfully loaded PCAP file',
        'Extracted HTTP payloads from network traffic',
        'Applied feature extraction algorithm',
        'Ran machine learning model analysis',
        isDetected ? 'SQL injection patterns detected' : 'No suspicious patterns found',
        'Generated security report'
      ],
      filename: file.name,
      size: file.size,
      packetsAnalyzed: Math.floor(Math.random() * 1000) + 100,
      threatsFound: isDetected ? Math.floor(Math.random() * 5) + 1 : 0,
      confidence: Math.floor(Math.random() * 20) + 80 // 80-100% confidence
    };

    return NextResponse.json(mockResult);
  } catch (error) {
    console.error('Error processing file:', error);
    return NextResponse.json(
      { error: 'Failed to process file. Please try again.' }, 
      { status: 500 }
    );
  }
}