class BoundedBlockingQueue {
    
    final Semaphore semaphore;
    final Queue<Integer> queue = new LinkedList<Integer>();

    public BoundedBlockingQueue(int capacity) {
        semaphore = new Semaphore(capacity);
    }
    
    public void enqueue(int element) throws InterruptedException {
        semaphore.acquire();
        synchronized (queue) {
            queue.add(element);
            queue.notify();
        }
    }
    
    public int dequeue() throws InterruptedException {
        int element;
        synchronized(queue){
            while(queue.isEmpty()){
                queue.wait();
            }
            element = queue.poll();
        }
        semaphore.release();
        return element; 
    }
    
    public int size() {
         synchronized(queue){
             return queue.size();
         }
    }
}